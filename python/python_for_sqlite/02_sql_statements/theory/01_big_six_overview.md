# Module 2: Big-6 SQL Statements Mastery
**Chapter 1: Overview and Fundamentals**

---

## The Big-6 SQL Statements

The "Big-6" SQL statements form the core of database operations. Master these, and you'll handle 95% of all database tasks effectively.

### **The Essential Six:**
1. **SELECT** - Query and retrieve data
2. **INSERT** - Add new data
3. **UPDATE** - Modify existing data
4. **DELETE** - Remove data
5. **CREATE TABLE** - Define database structure
6. **DROP TABLE** - Remove database objects

---

## SELECT Statement: Data Retrieval Master

### **Basic SELECT Syntax**
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
ORDER BY column
LIMIT count;
```

### **Python Integration Examples**
```python
# Basic SELECT
cursor.execute("SELECT name, email FROM customers")
results = cursor.fetchall()

# Parameterized SELECT (secure)
cursor.execute(
    "SELECT * FROM products WHERE price > ?", 
    (min_price,)
)

# SELECT with multiple conditions
cursor.execute("""
    SELECT name, price FROM products 
    WHERE category = ? AND stock > ?
    ORDER BY price DESC
""", ('Electronics', 10))
```

### **Advanced SELECT Patterns**
```sql
-- Subqueries
SELECT name FROM customers 
WHERE id IN (SELECT customer_id FROM orders WHERE total > 1000);

-- JOINs
SELECT c.name, o.order_date, o.total
FROM customers c
JOIN orders o ON c.id = o.customer_id;

-- Window functions
SELECT name, price,
       ROW_NUMBER() OVER (PARTITION BY category ORDER BY price) as rank
FROM products;
```

---

## INSERT Statement: Data Creation

### **INSERT Variations**
```sql
-- Single row insert
INSERT INTO customers (name, email) VALUES ('John Doe', 'john@example.com');

-- Multiple rows insert
INSERT INTO products (name, price, category) VALUES 
    ('Laptop', 999.99, 'Electronics'),
    ('Mouse', 29.99, 'Electronics'),
    ('Book', 19.99, 'Education');

-- Insert from SELECT
INSERT INTO backup_customers 
SELECT * FROM customers WHERE created_date < '2024-01-01';
```

### **Python INSERT Patterns**
```python
# Single insert
cursor.execute("""
    INSERT INTO customers (name, email, phone) 
    VALUES (?, ?, ?)
""", ('Jane Smith', 'jane@example.com', '555-0123'))

# Bulk insert (efficient)
data = [
    ('Product A', 99.99, 'Category1'),
    ('Product B', 149.99, 'Category2'),
    ('Product C', 79.99, 'Category1')
]
cursor.executemany("""
    INSERT INTO products (name, price, category) VALUES (?, ?, ?)
""", data)

# INSERT with RETURNING (get generated IDs)
cursor.execute("""
    INSERT INTO customers (name, email) VALUES (?, ?) 
    RETURNING id
""", ('New Customer', 'new@example.com'))
new_id = cursor.fetchone()[0]
```

---

## UPDATE Statement: Data Modification

### **UPDATE Syntax and Patterns**
```sql
-- Basic update
UPDATE customers 
SET email = 'newemail@example.com' 
WHERE id = 1;

-- Multiple column update
UPDATE products 
SET price = price * 1.1, stock = stock - 1
WHERE category = 'Electronics';

-- Conditional update
UPDATE customers 
SET status = CASE 
    WHEN total_orders > 10 THEN 'Premium'
    WHEN total_orders > 5 THEN 'Regular'
    ELSE 'New'
END;
```

### **Python UPDATE Safety**
```python
# Safe parameterized update
def update_customer_email(cursor, customer_id, new_email):
    cursor.execute("""
        UPDATE customers 
        SET email = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (new_email, customer_id))
    
    if cursor.rowcount == 0:
        raise ValueError(f"Customer {customer_id} not found")
    
    return cursor.rowcount

# Bulk update with validation
def apply_discount(cursor, category, discount_percent):
    cursor.execute("""
        UPDATE products 
        SET price = ROUND(price * (1 - ? / 100.0), 2)
        WHERE category = ? AND price > 0
    """, (discount_percent, category))
    
    return cursor.rowcount
```

---

## DELETE Statement: Data Removal

### **DELETE Variations**
```sql
-- Simple delete
DELETE FROM customers WHERE id = 1;

-- Conditional delete
DELETE FROM orders WHERE order_date < '2023-01-01';

-- Delete with subquery
DELETE FROM products 
WHERE id NOT IN (SELECT DISTINCT product_id FROM order_items);
```

### **Safe DELETE Patterns**
```python
def safe_delete_customer(cursor, customer_id):
    """Safely delete customer with dependency checks"""
    
    # Check for existing orders
    cursor.execute(
        "SELECT COUNT(*) FROM orders WHERE customer_id = ?", 
        (customer_id,)
    )
    order_count = cursor.fetchone()[0]
    
    if order_count > 0:
        raise ValueError(f"Cannot delete customer {customer_id}: has {order_count} orders")
    
    # Safe to delete
    cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
    
    if cursor.rowcount == 0:
        raise ValueError(f"Customer {customer_id} not found")
    
    return cursor.rowcount

# Soft delete pattern
def soft_delete_customer(cursor, customer_id):
    """Mark customer as deleted instead of removing"""
    cursor.execute("""
        UPDATE customers 
        SET is_deleted = 1, deleted_at = CURRENT_TIMESTAMP
        WHERE id = ? AND is_deleted = 0
    """, (customer_id,))
    
    return cursor.rowcount
```

---

## CREATE TABLE: Schema Definition

### **Comprehensive TABLE Creation**
```sql
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    address JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    credit_limit DECIMAL(10,2) DEFAULT 1000.00,
    
    -- Constraints
    CHECK (length(name) > 0),
    CHECK (email LIKE '%@%.%'),
    CHECK (credit_limit >= 0)
);

-- Indexes for performance
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_customers_active ON customers(is_active, created_at);
```

### **Python Schema Management**
```python
class SchemaManager:
    """Manage database schema creation and migration"""
    
    def __init__(self, connection):
        self.conn = connection
    
    def create_customers_table(self):
        """Create customers table with all constraints"""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL CHECK(length(trim(name)) > 0),
                email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
                phone TEXT,
                address JSON,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT 1,
                credit_limit DECIMAL(10,2) DEFAULT 1000.00 CHECK(credit_limit >= 0)
            )
        """)
        
        # Create indexes
        indexes = [
            "CREATE INDEX IF NOT EXISTS idx_customers_email ON customers(email)",
            "CREATE INDEX IF NOT EXISTS idx_customers_active ON customers(is_active)",
        ]
        
        for index in indexes:
            self.conn.execute(index)
    
    def create_all_tables(self):
        """Create complete schema"""
        self.create_customers_table()
        # ... other table creation methods
        self.conn.commit()
```

---

## DROP TABLE: Schema Cleanup

### **Safe DROP Patterns**
```sql
-- Simple drop
DROP TABLE IF EXISTS temp_table;

-- Drop with dependency check
DROP TABLE customers; -- Will fail if foreign key references exist
```

### **Python DROP Management**
```python
def safe_drop_table(cursor, table_name):
    """Safely drop table with dependency checks"""
    
    # Check for foreign key references
    cursor.execute("""
        SELECT sql FROM sqlite_master 
        WHERE type = 'table' AND sql LIKE '%REFERENCES %' || ? || '%'
    """, (table_name,))
    
    references = cursor.fetchall()
    if references:
        ref_tables = [ref[0] for ref in references]
        raise ValueError(f"Cannot drop {table_name}: referenced by {ref_tables}")
    
    # Safe to drop
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    
    return cursor.rowcount

def backup_and_drop(cursor, table_name):
    """Create backup before dropping table"""
    backup_name = f"{table_name}_backup_{int(time.time())}"
    
    # Create backup
    cursor.execute(f"CREATE TABLE {backup_name} AS SELECT * FROM {table_name}")
    
    # Drop original
    cursor.execute(f"DROP TABLE {table_name}")
    
    return backup_name
```

---

## Performance Optimization for Big-6

### **Query Optimization Tips**
```python
# Use EXPLAIN QUERY PLAN to analyze performance
def analyze_query(cursor, query, params=None):
    """Analyze query performance"""
    plan_query = f"EXPLAIN QUERY PLAN {query}"
    
    if params:
        cursor.execute(plan_query, params)
    else:
        cursor.execute(plan_query)
    
    plan = cursor.fetchall()
    for step in plan:
        print(f"{step[0]}|{step[1]}|{step[2]}|{step[3]}")

# Batch operations for better performance
def efficient_bulk_operations(cursor):
    """Demonstrate efficient bulk operations"""
    
    # Wrap in transaction
    cursor.execute("BEGIN TRANSACTION")
    
    try:
        # Bulk insert
        data = [(f"Customer {i}", f"email{i}@example.com") for i in range(1000)]
        cursor.executemany(
            "INSERT INTO customers (name, email) VALUES (?, ?)", 
            data
        )
        
        # Bulk update
        cursor.execute(
            "UPDATE customers SET is_active = 1 WHERE created_at > datetime('now', '-1 day')"
        )
        
        cursor.execute("COMMIT")
        print(f"Bulk operation completed successfully")
        
    except Exception as e:
        cursor.execute("ROLLBACK")
        raise e
```

---

## Common Patterns and Best Practices

### **UPSERT Pattern (INSERT OR UPDATE)**
```sql
-- SQLite UPSERT syntax
INSERT INTO products (id, name, price) VALUES (1, 'Updated Product', 199.99)
ON CONFLICT(id) DO UPDATE SET 
    name = excluded.name,
    price = excluded.price,
    updated_at = CURRENT_TIMESTAMP;
```

### **Pagination Pattern**
```python
def paginate_results(cursor, table, page_size=20, page_number=1):
    """Implement efficient pagination"""
    offset = (page_number - 1) * page_size
    
    # Get total count
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    total_count = cursor.fetchone()[0]
    
    # Get page data
    cursor.execute(f"""
        SELECT * FROM {table} 
        ORDER BY id 
        LIMIT ? OFFSET ?
    """, (page_size, offset))
    
    results = cursor.fetchall()
    
    return {
        'data': results,
        'page': page_number,
        'page_size': page_size,
        'total_count': total_count,
        'total_pages': (total_count + page_size - 1) // page_size
    }
```

### **Audit Trail Pattern**
```python
def create_audit_trigger(cursor, table_name):
    """Create audit trail for table changes"""
    
    # Create audit table
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name}_audit (
            audit_id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_name TEXT NOT NULL,
            operation TEXT NOT NULL,
            old_values JSON,
            new_values JSON,
            changed_by TEXT,
            changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create triggers for INSERT, UPDATE, DELETE
    triggers = [
        ("INSERT", "NEW", None),
        ("UPDATE", "NEW", "OLD"), 
        ("DELETE", None, "OLD")
    ]
    
    for operation, new_ref, old_ref in triggers:
        trigger_name = f"{table_name}_{operation.lower()}_audit"
        
        cursor.execute(f"""
            CREATE TRIGGER IF NOT EXISTS {trigger_name}
            AFTER {operation} ON {table_name}
            BEGIN
                INSERT INTO {table_name}_audit (table_name, operation, old_values, new_values)
                VALUES ('{table_name}', '{operation}', 
                       {f"json_object('id', {old_ref}.id)" if old_ref else "NULL"},
                       {f"json_object('id', {new_ref}.id)" if new_ref else "NULL"});
            END;
        """)
```

**Next Chapter**: Hands-on implementation of all Big-6 statements with real-world scenarios!