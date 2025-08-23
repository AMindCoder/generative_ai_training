# Module 4: Pandas Integration & Structured Reporting
**Chapter 1: SQLite to Pandas Workflow**

---

## Core Integration Patterns

### **Database to DataFrame**
```python
import pandas as pd
import sqlite3

# Direct query to DataFrame
df = pd.read_sql_query("""
    SELECT c.name, COUNT(o.id) as orders, SUM(o.total) as revenue
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    GROUP BY c.id, c.name
""", conn)

# DataFrame operations
df['avg_order'] = df['revenue'] / df['orders']
df_sorted = df.sort_values('revenue', ascending=False)
```

### **DataFrame to Database**
```python
# Write DataFrame to SQLite
df.to_sql('customer_summary', conn, if_exists='replace', index=False)

# Append data
new_data.to_sql('sales_data', conn, if_exists='append', index=False)
```

### **Advanced Data Processing**
```python
# Complex data transformation pipeline
def create_monthly_report(conn, year, month):
    # Extract data
    df = pd.read_sql_query(f"""
        SELECT * FROM orders 
        WHERE strftime('%Y-%m', order_date) = '{year}-{month:02d}'
    """, conn)
    
    # Transform
    df['order_month'] = pd.to_datetime(df['order_date']).dt.month
    df['revenue_category'] = pd.cut(df['total_amount'], 
                                   bins=[0, 100, 500, 1000, float('inf')],
                                   labels=['Low', 'Medium', 'High', 'Premium'])
    
    # Aggregate
    summary = df.groupby('revenue_category').agg({
        'id': 'count',
        'total_amount': ['sum', 'mean', 'std']
    }).round(2)
    
    return summary
```

### **Memory-Efficient Processing**
```python
# Process large datasets in chunks
def process_large_table(conn, table_name, chunk_size=10000):
    query = f"SELECT COUNT(*) FROM {table_name}"
    total_rows = pd.read_sql_query(query, conn).iloc[0, 0]
    
    results = []
    for offset in range(0, total_rows, chunk_size):
        chunk_query = f"""
            SELECT * FROM {table_name} 
            LIMIT {chunk_size} OFFSET {offset}
        """
        chunk_df = pd.read_sql_query(chunk_query, conn)
        
        # Process chunk
        processed = chunk_df.groupby('category')['amount'].sum()
        results.append(processed)
    
    # Combine results
    final_result = pd.concat(results).groupby(level=0).sum()
    return final_result
```

**Next**: Building comprehensive reporting dashboards!