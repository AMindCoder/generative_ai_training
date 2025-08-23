# Module 5: Data Visualization with Matplotlib & Seaborn
**Chapter 1: Database to Visualization Pipeline**

---

## Direct Database to Visualization

### **SQLite → Matplotlib Pipeline**
```python
import matplotlib.pyplot as plt
import pandas as pd

def create_sales_dashboard(conn):
    # Query data directly from database
    df = pd.read_sql_query("""
        SELECT 
            strftime('%Y-%m', order_date) as month,
            SUM(total_amount) as revenue,
            COUNT(*) as order_count
        FROM orders
        GROUP BY strftime('%Y-%m', order_date)
        ORDER BY month
    """, conn)
    
    # Create dashboard
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Revenue trend
    ax1.plot(df['month'], df['revenue'], marker='o', linewidth=2)
    ax1.set_title('Monthly Revenue Trend')
    ax1.tick_params(axis='x', rotation=45)
    
    # Order count bars
    ax2.bar(df['month'], df['order_count'], color='steelblue')
    ax2.set_title('Monthly Order Count')
    
    plt.tight_layout()
    return fig
```

### **Advanced Seaborn Analytics**
```python
import seaborn as sns

def create_customer_analysis(conn):
    # Complex query with customer segmentation
    df = pd.read_sql_query("""
        SELECT 
            c.customer_type,
            c.credit_limit,
            COUNT(o.id) as order_count,
            SUM(o.total_amount) as lifetime_value,
            AVG(o.total_amount) as avg_order
        FROM customers c
        LEFT JOIN orders o ON c.id = o.customer_id
        GROUP BY c.id, c.customer_type, c.credit_limit
    """, conn)
    
    # Advanced visualizations
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # Customer type distribution
    sns.countplot(data=df, x='customer_type', ax=axes[0, 0])
    
    # Lifetime value by type
    sns.boxplot(data=df, x='customer_type', y='lifetime_value', ax=axes[0, 1])
    
    # Credit limit vs lifetime value
    sns.scatterplot(data=df, x='credit_limit', y='lifetime_value', 
                   hue='customer_type', size='order_count', ax=axes[0, 2])
    
    return fig
```

### **Interactive Dashboards**
```python
def create_interactive_dashboard(conn):
    """Create interactive dashboard with real-time data updates"""
    
    # Real-time data query
    current_data = pd.read_sql_query("""
        SELECT 
            p.category,
            p.name,
            p.price,
            p.stock_quantity,
            COALESCE(sales.quantity_sold, 0) as sold
        FROM products p
        LEFT JOIN (
            SELECT product_id, SUM(quantity) as quantity_sold
            FROM order_items oi
            JOIN orders o ON oi.order_id = o.id
            WHERE o.order_date >= date('now', '-30 days')
            GROUP BY product_id
        ) sales ON p.id = sales.product_id
    """, conn)
    
    # Create dynamic visualizations
    return create_product_performance_charts(current_data)
```

### **Export and Reporting**
```python
def generate_automated_report(conn, output_path):
    """Generate automated PDF report with charts"""
    
    from matplotlib.backends.backend_pdf import PdfPages
    
    with PdfPages(output_path) as pdf:
        # Page 1: Executive Summary
        fig1 = create_executive_summary(conn)
        pdf.savefig(fig1, bbox_inches='tight')
        
        # Page 2: Sales Analysis
        fig2 = create_sales_analysis(conn)
        pdf.savefig(fig2, bbox_inches='tight')
        
        # Page 3: Customer Insights
        fig3 = create_customer_insights(conn)
        pdf.savefig(fig3, bbox_inches='tight')
        
    print(f"Report generated: {output_path}")
```

**Next**: Building complete visualization dashboards with interactive features!