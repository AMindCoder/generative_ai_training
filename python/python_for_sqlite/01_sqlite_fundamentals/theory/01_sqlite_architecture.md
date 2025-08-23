# Module 1: SQLite Fundamentals with Python
**Chapter 1: SQLite Architecture and Core Concepts**

---

## Understanding SQLite Architecture

SQLite's unique architecture makes it the world's most deployed database engine. Let's explore how it works under the hood and why it's perfect for Python integration.

---

### **SQLite Architecture Overview**

```
┌─────────────────────────────────────────────────────┐
│                SQL Interface                        │
├─────────────────────────────────────────────────────┤
│                SQL Command Processor                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   Parser    │  │ Code Gen    │  │ Virtual     │ │
│  │             │  │             │  │ Machine     │ │
│  └─────────────┘  └─────────────┘  └─────────────┘ │
├─────────────────────────────────────────────────────┤
│                    Backend                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   B-Tree    │  │    Pager    │  │   OS        │ │
│  │             │  │             │  │ Interface   │ │
│  └─────────────┘  └─────────────┘  └─────────────┘ │
└─────────────────────────────────────────────────────┘
```

---

### **Core Components Deep Dive**

#### **1. SQL Command Processor**

**Parser**: Converts SQL text into parse tree
```python
# When you write this SQL:
cursor.execute("SELECT name FROM users WHERE age > 25")

# Parser creates a tree structure representing:
# SELECT -> name (column)
# FROM -> users (table)  
# WHERE -> age > 25 (condition)
```

**Code Generator**: Converts parse tree into bytecode
```python
# Bytecode operations (simplified):
# OpenRead 0 2 0          # Open table users
# Rewind 0                # Go to first record
# Column 0 1              # Read age column
# Ge 25                   # Check if >= 25
# Column 0 0              # Read name column
# ResultRow               # Output result
```

**Virtual Machine**: Executes bytecode operations
- Stack-based architecture
- Highly optimized for database operations
- Handles transactions, locking, and data integrity

#### **2. Backend Storage**

**B-Tree Module**: Core data structure for all storage
```
B-Tree Structure in SQLite:
┌─────────────────────────────────────────┐
│              Root Page                  │
│  [10] [20] [30] [40]                   │
│   │    │    │    │                     │
├───┘    │    │    └─────────────────────┤
│ [5][8] │    │              [45][48]    │
│        │    │                          │
│   [15][18]  │                          │
│             │                          │
│        [25][28]                        │
└─────────────────────────────────────────┘
```

**Pager**: Manages memory and disk I/O
- Handles page caching
- Manages transactions and rollback
- Implements locking mechanisms
- Optimizes disk access patterns

**OS Interface**: Platform-specific operations
- File I/O operations
- Locking mechanisms
- Memory allocation
- Thread synchronization

---

### **SQLite File Format**

#### **Database File Structure**
```
SQLite Database File:
┌─────────────────────┐ ← File Header (100 bytes)
├─────────────────────┤
│   Page 1 (Schema)   │ ← sqlite_master table
├─────────────────────┤
│   Page 2 (Data)     │ ← User tables and indexes
├─────────────────────┤
│   Page 3 (Data)     │
├─────────────────────┤
│        ...          │
├─────────────────────┤
│   Page N (Data)     │ ← Last page
└─────────────────────┘
```

#### **File Header Information**
```python
import sqlite3

def examine_database_header(db_path):
    """Examine SQLite database header information"""
    with open(db_path, 'rb') as f:
        header = f.read(100)  # First 100 bytes
        
        # Magic header string
        magic = header[0:16].decode('utf-8', errors='ignore')
        
        # Page size (bytes 16-17)
        page_size = int.from_bytes(header[16:18], 'big')
        
        # File format versions
        write_version = header[18]
        read_version = header[19]
        
        # Database page count
        page_count = int.from_bytes(header[28:32], 'big')
        
        return {
            'magic': magic,
            'page_size': page_size,
            'write_version': write_version,
            'read_version': read_version,
            'page_count': page_count,
            'file_size': page_count * page_size
        }

# Usage example (we'll use this in the lab)
# header_info = examine_database_header('example.db')
```

---

### **Storage Classes vs Data Types**

SQLite uses **storage classes** instead of rigid data types:

#### **Storage Classes:**
1. **NULL**: The value is NULL
2. **INTEGER**: Signed integers (variable length: 1,2,3,4,6,8 bytes)
3. **REAL**: 8-byte IEEE floating point numbers
4. **TEXT**: UTF-8, UTF-16BE, or UTF-16LE text strings
5. **BLOB**: Binary Large Object (stored as-is)

#### **Type Affinity Rules:**
```sql
-- Column affinity determines preferred storage class
CREATE TABLE example_types (
    id INTEGER,        -- INTEGER affinity
    name TEXT,         -- TEXT affinity  
    price REAL,        -- REAL affinity
    data BLOB,         -- No affinity
    timestamp NUMERIC  -- NUMERIC affinity
);
```

#### **Python Type Mapping:**
```python
# Python to SQLite type conversion
python_to_sqlite = {
    int: 'INTEGER',
    float: 'REAL', 
    str: 'TEXT',
    bytes: 'BLOB',
    type(None): 'NULL'
}

# SQLite to Python type conversion  
sqlite_to_python = {
    'INTEGER': int,
    'REAL': float,
    'TEXT': str, 
    'BLOB': bytes,
    'NULL': type(None)
}
```

---

### **Transaction Processing**

#### **ACID Properties Implementation**

**Atomicity**: All-or-nothing transactions
```python
try:
    conn.execute("BEGIN TRANSACTION")
    conn.execute("INSERT INTO accounts VALUES (1, 100)")
    conn.execute("INSERT INTO accounts VALUES (2, 200)")
    conn.execute("COMMIT")
except Exception as e:
    conn.execute("ROLLBACK")
    print(f"Transaction failed: {e}")
```

**Consistency**: Database rules are always enforced
```sql
-- Foreign key constraints maintain consistency
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    total REAL CHECK(total >= 0)
);
```

**Isolation**: Transactions don't interfere with each other
```python
# SQLite supports multiple isolation levels
conn.execute("PRAGMA read_uncommitted = 1")  # Read Uncommitted
# Default is Serializable isolation
```

**Durability**: Committed changes persist
```python
# WAL mode provides better durability and concurrency
conn.execute("PRAGMA journal_mode = WAL")
```

---

### **Locking and Concurrency**

#### **SQLite Locking States**
1. **UNLOCKED**: No locks held
2. **SHARED**: Reading allowed, writing blocked  
3. **RESERVED**: Preparing to write
4. **PENDING**: Waiting for readers to finish
5. **EXCLUSIVE**: Only one connection can access

#### **Practical Concurrency Example**
```python
import sqlite3
import threading
import time

def reader_worker(db_path, worker_id):
    """Simulates concurrent reading"""
    conn = sqlite3.connect(db_path)
    for i in range(5):
        cursor = conn.execute("SELECT COUNT(*) FROM users")
        count = cursor.fetchone()[0]
        print(f"Reader {worker_id}: Found {count} users")
        time.sleep(0.1)
    conn.close()

def writer_worker(db_path, worker_id):
    """Simulates concurrent writing"""
    conn = sqlite3.connect(db_path)
    try:
        for i in range(3):
            conn.execute("INSERT INTO users (name) VALUES (?)", 
                        (f"User-{worker_id}-{i}",))
            conn.commit()
            print(f"Writer {worker_id}: Inserted user {i}")
            time.sleep(0.2)
    except sqlite3.OperationalError as e:
        print(f"Writer {worker_id} failed: {e}")
    finally:
        conn.close()
```

---

### **Performance Characteristics**

#### **SQLite Strengths**
- **Read Performance**: Extremely fast for read operations
- **Local Access**: No network latency
- **Cache Efficiency**: Intelligent page caching
- **Query Optimization**: Cost-based query planner

#### **Performance Benchmarks**
```python
import time
import sqlite3

def benchmark_operations(db_path, num_records=10000):
    """Benchmark basic SQLite operations"""
    conn = sqlite3.connect(db_path)
    
    # Create test table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS benchmark (
            id INTEGER PRIMARY KEY,
            data TEXT,
            number REAL
        )
    ''')
    
    # Benchmark INSERT operations
    start_time = time.time()
    for i in range(num_records):
        conn.execute("INSERT INTO benchmark (data, number) VALUES (?, ?)",
                    (f"Record {i}", i * 1.5))
    conn.commit()
    insert_time = time.time() - start_time
    
    # Benchmark SELECT operations  
    start_time = time.time()
    cursor = conn.execute("SELECT * FROM benchmark WHERE number > ?", (5000,))
    results = cursor.fetchall()
    select_time = time.time() - start_time
    
    conn.close()
    
    return {
        'insert_time': insert_time,
        'select_time': select_time,
        'records_inserted': num_records,
        'records_selected': len(results)
    }
```

---

### **Memory Management**

#### **Page Cache Configuration**
```python
def optimize_sqlite_performance(conn):
    """Apply performance optimizations"""
    
    # Increase cache size (default is 2MB)
    conn.execute("PRAGMA cache_size = 10000")  # 10MB cache
    
    # Use WAL mode for better concurrency
    conn.execute("PRAGMA journal_mode = WAL")
    
    # Optimize synchronization
    conn.execute("PRAGMA synchronous = NORMAL")  # Balanced safety/speed
    
    # Temporary storage in memory
    conn.execute("PRAGMA temp_store = MEMORY")
    
    # Memory-mapped I/O (for large databases)
    conn.execute("PRAGMA mmap_size = 268435456")  # 256MB mmap
    
    return conn
```

#### **Memory Usage Monitoring**
```python
def check_memory_usage(conn):
    """Monitor SQLite memory usage"""
    
    # Page cache hit ratio
    cache_stats = conn.execute("PRAGMA cache_size").fetchone()[0]
    
    # Database page count and size
    page_count = conn.execute("PRAGMA page_count").fetchone()[0]
    page_size = conn.execute("PRAGMA page_size").fetchone()[0]
    
    # Current memory usage
    memory_used = conn.execute("PRAGMA cache_size").fetchone()[0] * page_size
    
    return {
        'cache_size_pages': cache_stats,
        'total_pages': page_count,
        'page_size_bytes': page_size,
        'estimated_memory_mb': memory_used / (1024 * 1024)
    }
```

---

### **Schema Storage and Metadata**

#### **sqlite_master Table**
SQLite stores all schema information in a special table:

```sql
-- The sqlite_master table structure
CREATE TABLE sqlite_master (
    type TEXT,        -- 'table', 'index', 'view', 'trigger'
    name TEXT,        -- Object name  
    tbl_name TEXT,    -- Associated table name
    rootpage INTEGER, -- Root page number in database file
    sql TEXT          -- Original CREATE statement
);
```

#### **Querying Schema Information**
```python
def analyze_database_schema(conn):
    """Analyze database schema and structure"""
    
    # Get all tables
    tables = conn.execute("""
        SELECT name, sql FROM sqlite_master 
        WHERE type = 'table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name
    """).fetchall()
    
    # Get all indexes
    indexes = conn.execute("""
        SELECT name, tbl_name, sql FROM sqlite_master
        WHERE type = 'index' AND name NOT LIKE 'sqlite_%'
        ORDER BY tbl_name, name  
    """).fetchall()
    
    # Get database statistics
    stats = {}
    for table_name, _ in tables:
        count = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
        stats[table_name] = count
    
    return {
        'tables': tables,
        'indexes': indexes, 
        'record_counts': stats
    }
```

---

### **Advanced SQLite Features**

#### **Full-Text Search (FTS)**
```sql
-- Create FTS virtual table
CREATE VIRTUAL TABLE documents_fts USING fts5(
    title, content, author
);

-- Insert data
INSERT INTO documents_fts VALUES 
('SQLite Guide', 'Complete guide to SQLite database', 'John Doe'),
('Python Tutorial', 'Learn Python programming', 'Jane Smith');

-- Full-text search
SELECT * FROM documents_fts WHERE documents_fts MATCH 'sqlite OR python';
```

#### **JSON Support (SQLite 3.38+)**
```sql
-- JSON data storage and querying
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    attributes JSON
);

INSERT INTO products VALUES (
    1, 'Laptop', 
    '{"brand": "Dell", "ram": "16GB", "storage": "512GB SSD"}'
);

-- Query JSON data
SELECT name, json_extract(attributes, '$.brand') as brand
FROM products 
WHERE json_extract(attributes, '$.ram') = '16GB';
```

#### **Window Functions**
```sql
-- Advanced analytics with window functions
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) as running_total,
    AVG(amount) OVER (ORDER BY date ROWS 2 PRECEDING) as moving_avg
FROM expenses
ORDER BY date;
```

---

### **SQLite vs Other Databases: Technical Comparison**

| Aspect | SQLite | MySQL | PostgreSQL | MongoDB |
|--------|--------|--------|------------|---------|
| **Architecture** | Embedded | Client-Server | Client-Server | Client-Server |
| **Storage Engine** | Single B-Tree | Multiple (InnoDB, MyISAM) | Single | Document Store |
| **Max DB Size** | 281 TB | Unlimited | Unlimited | Unlimited |
| **Max Row Size** | 1 GB | 65,535 bytes | 1.6 TB | 16 MB |
| **Joins** | Full SQL | Full SQL | Full SQL | Limited |
| **Transactions** | ACID | ACID | ACID | ACID (4.0+) |
| **Concurrent Writes** | 1 | Many | Many | Many |
| **Setup Complexity** | None | Medium | High | Medium |

---

### **When to Choose SQLite**

#### **Perfect Use Cases:**
- **Desktop Applications**: Configuration, local data
- **Mobile Applications**: Offline-first architecture
- **Prototyping**: Rapid development and testing
- **Data Analysis**: Local data processing
- **Edge Computing**: IoT devices, embedded systems
- **Content Management**: Read-heavy applications

#### **Consider Alternatives When:**
- High concurrent write loads (>100 writes/sec)
- Multi-user web applications
- Distributed systems requirements
- Complex stored procedures needed
- Advanced user management required

---

### **Python sqlite3 Module Deep Dive**

#### **Module Architecture**
```python
import sqlite3

# The sqlite3 module provides:
# - Connection objects (sqlite3.Connection)
# - Cursor objects (sqlite3.Cursor)  
# - Row objects (sqlite3.Row)
# - Exception hierarchy
# - Type adapters and converters

# Key classes and their relationships:
# Connection -> Cursor -> Results
```

#### **Connection Object Methods**
```python
connection_methods = {
    'execute()': 'Execute single SQL statement',
    'executemany()': 'Execute SQL with multiple parameter sets',
    'executescript()': 'Execute multiple SQL statements',
    'commit()': 'Commit current transaction',
    'rollback()': 'Rollback current transaction', 
    'close()': 'Close database connection',
    'cursor()': 'Create new cursor object',
    'backup()': 'Backup database to another database',
    'create_function()': 'Create user-defined SQL function',
    'create_aggregate()': 'Create user-defined aggregate function'
}
```

---

### **Preparation for Next Chapter**

In Chapter 2, we'll explore:
- Python sqlite3 module in detail
- Connection management patterns
- Error handling strategies
- Transaction management
- Performance optimization techniques

**Coming Up**: Hands-on implementation of SQLite fundamentals with Python!