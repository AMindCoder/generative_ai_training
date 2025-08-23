# Module 3: Aggregate Functions & Data Analysis
**Chapter 1: Mastering Aggregate Functions**

---

## Core Aggregate Functions

### **The Essential Five**
1. **COUNT()** - Count records
2. **SUM()** - Total numeric values  
3. **AVG()** - Average values
4. **MIN()** - Minimum value
5. **MAX()** - Maximum value

### **Advanced Aggregations**
- **GROUP BY** - Group data for aggregation
- **HAVING** - Filter aggregated results
- **Window Functions** - Advanced analytics
- **Custom Aggregations** - Python-defined functions

---

## Python Integration Examples

```python
# Sales analytics example
cursor.execute("""
    SELECT 
        strftime('%Y-%m', order_date) as month,
        COUNT(*) as order_count,
        SUM(total_amount) as revenue,
        AVG(total_amount) as avg_order,
        MIN(total_amount) as min_order,
        MAX(total_amount) as max_order
    FROM orders 
    WHERE status = 'completed'
    GROUP BY strftime('%Y-%m', order_date)
    HAVING revenue > 1000
    ORDER BY month DESC
""")

for row in cursor.fetchall():
    print(f"{row['month']}: {row['order_count']} orders, ${row['revenue']:.2f} revenue")
```

### **Window Functions for Advanced Analytics**
```sql
-- Running totals and rankings
SELECT 
    customer_name,
    order_date,
    amount,
    SUM(amount) OVER (PARTITION BY customer_id ORDER BY order_date) as running_total,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) as rank_by_amount,
    AVG(amount) OVER (ORDER BY order_date ROWS 2 PRECEDING) as moving_avg
FROM orders;
```

### **Custom Aggregate Functions**
```python
class StandardDeviation:
    def __init__(self):
        self.values = []
    
    def step(self, value):
        if value is not None:
            self.values.append(value)
    
    def finalize(self):
        if len(self.values) < 2:
            return None
        mean = sum(self.values) / len(self.values)
        variance = sum((x - mean) ** 2 for x in self.values) / len(self.values)
        return math.sqrt(variance)

# Register custom aggregate
conn.create_aggregate("STDDEV", 1, StandardDeviation)
```

**Next**: Hands-on implementation of comprehensive data analysis!