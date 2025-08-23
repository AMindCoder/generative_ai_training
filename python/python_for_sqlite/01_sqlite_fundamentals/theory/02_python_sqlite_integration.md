# Module 1: SQLite Fundamentals with Python
**Chapter 2: Python sqlite3 Module Mastery**

---

## Deep Dive into Python's sqlite3 Module

The `sqlite3` module is Python's gateway to SQLite databases. This chapter covers everything from basic usage to advanced patterns that professional developers use in production systems.

---

### **Module Import and Basic Setup**

```python
import sqlite3
import sys
from datetime import datetime, date
from decimal import Decimal
from pathlib import Path

# Check sqlite3 module information
print(f"sqlite3 module version: {sqlite3.version}")
print(f"SQLite library version: {sqlite3.sqlite_version}")
print(f"sqlite3 threadsafety: {sqlite3.threadsafety}")
```

---

### **Connection Objects: The Foundation**

#### **Creating Connections**

```python
# Method 1: File-based database
conn = sqlite3.connect('example.db')

# Method 2: In-memory database (temporary)
conn = sqlite3.connect(':memory:')

# Method 3: URI connections (advanced)
conn = sqlite3.connect('file:example.db?mode=rwc&cache=shared&uri=true')

# Method 4: Connection with parameters
conn = sqlite3.connect(
    database='example.db',
    timeout=30.0,           # 30-second timeout
    detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
    isolation_level='DEFERRED',  # Transaction behavior
    check_same_thread=False      # Thread safety
)
```

#### **Connection Parameters Explained**

**timeout**: How long to wait for locks to clear
```python
# If another connection is writing, wait up to 30 seconds
conn = sqlite3.connect('busy_database.db', timeout=30.0)
```

**detect_types**: Automatic Python type conversion
```python
# Parse declared column types and column names for type hints
conn = sqlite3.connect(
    'database.db', 
    detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
)

# Now datetime objects are automatically converted
conn.execute("INSERT INTO events (date) VALUES (?)", (datetime.now(),))
```

**isolation_level**: Transaction behavior
```python
# None = autocommit mode (no transactions)
conn = sqlite3.connect('database.db', isolation_level=None)

# 'DEFERRED' = default, transaction starts when needed
# 'IMMEDIATE' = transaction starts immediately  
# 'EXCLUSIVE' = exclusive transaction
```

---

### **Connection Management Patterns**

#### **1. Context Manager Pattern (Recommended)**
```python
def context_manager_example():
    """Best practice: Use context manager for automatic cleanup"""
    
    with sqlite3.connect('database.db') as conn:
        # Connection automatically managed
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Insert data
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            ('John Doe', 'john@example.com')
        )
        
        # Connection commits automatically if no exception
        # Connection closes automatically when exiting 'with' block
        
    # Connection is now closed
```

#### **2. Connection Pool Pattern**
```python
import threading
from queue import Queue

class SQLiteConnectionPool:
    """Thread-safe connection pool for SQLite"""
    
    def __init__(self, database_path, pool_size=5):
        self.database_path = database_path
        self.pool_size = pool_size
        self.pool = Queue(maxsize=pool_size)
        self._lock = threading.Lock()
        
        # Initialize pool
        for _ in range(pool_size):
            conn = sqlite3.connect(
                database_path, 
                check_same_thread=False,
                timeout=30.0
            )
            self.pool.put(conn)
    
    def get_connection(self):
        """Get connection from pool"""
        return self.pool.get()
    
    def return_connection(self, conn):
        """Return connection to pool"""
        self.pool.put(conn)
    
    def close_all(self):
        """Close all connections in pool"""
        while not self.pool.empty():
            conn = self.pool.get()
            conn.close()

# Usage example
pool = SQLiteConnectionPool('database.db')

def worker_function():
    conn = pool.get_connection()
    try:
        # Use connection
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        result = cursor.fetchone()
        print(f"User count: {result[0]}")
    finally:
        pool.return_connection(conn)
```

#### **3. Connection Factory Pattern**
```python
class DatabaseConnection:
    """Factory for creating configured database connections"""
    
    def __init__(self, database_path):
        self.database_path = database_path
        self.default_config = {
            'timeout': 30.0,
            'detect_types': sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
            'isolation_level': 'DEFERRED',
            'check_same_thread': False
        }
    
    def create_connection(self, config_overrides=None):
        """Create a configured connection"""
        config = self.default_config.copy()
        if config_overrides:
            config.update(config_overrides)
            
        conn = sqlite3.connect(self.database_path, **config)
        
        # Apply performance optimizations
        conn.execute("PRAGMA journal_mode = WAL")
        conn.execute("PRAGMA synchronous = NORMAL")
        conn.execute("PRAGMA cache_size = 10000")
        conn.execute("PRAGMA temp_store = MEMORY")
        
        return conn
    
    def create_readonly_connection(self):
        """Create read-only connection"""
        return self.create_connection({
            'isolation_level': None,  # Autocommit
        })

# Usage
db_factory = DatabaseConnection('app_database.db')
conn = db_factory.create_connection()
```

---

### **Cursor Objects: Data Access Interface**

#### **Cursor Creation and Methods**
```python
# Create cursor from connection
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Key cursor methods
cursor_methods = {
    'execute(sql, parameters)': 'Execute single SQL statement',
    'executemany(sql, seq_of_parameters)': 'Execute SQL multiple times',
    'executescript(sql_script)': 'Execute multiple SQL statements',
    'fetchone()': 'Fetch next row',
    'fetchmany(size)': 'Fetch specified number of rows',
    'fetchall()': 'Fetch all remaining rows',
    'close()': 'Close cursor'
}
```

#### **Parameter Substitution (SQL Injection Prevention)**
```python
# ✅ SECURE: Use parameter substitution
def secure_user_lookup(cursor, user_id):
    """Safe way to query with user input"""
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# ✅ SECURE: Named parameters
def secure_user_insert(cursor, name, email):
    """Safe way to insert with named parameters"""
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (:name, :email)",
        {'name': name, 'email': email}
    )

# ❌ INSECURE: Never do this!
def insecure_user_lookup(cursor, user_id):
    """Vulnerable to SQL injection"""
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchone()

# Example of SQL injection vulnerability:
malicious_input = "1; DROP TABLE users; --"
# insecure_user_lookup(cursor, malicious_input)  # Would delete users table!
```

#### **Batch Operations with executemany()**
```python
def efficient_bulk_insert():
    """Demonstrate efficient bulk data insertion"""
    
    with sqlite3.connect('bulk_data.db') as conn:
        cursor = conn.cursor()
        
        # Create test table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL,
                category TEXT
            )
        """)
        
        # Sample data
        products_data = [
            ('Laptop', 999.99, 'Electronics'),
            ('Mouse', 29.99, 'Electronics'),
            ('Book', 14.99, 'Education'),
            ('Pen', 2.50, 'Office'),
            ('Monitor', 299.99, 'Electronics')
        ]
        
        # Efficient bulk insert
        cursor.executemany(
            "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
            products_data
        )
        
        print(f"Inserted {cursor.rowcount} products")
        
        # Verify insertion
        cursor.execute("SELECT COUNT(*) FROM products")
        count = cursor.fetchone()[0]
        print(f"Total products in database: {count}")
```

---

### **Row Objects and Data Access Patterns**

#### **Default Tuple Rows**
```python
def default_row_access():
    """Default sqlite3 returns rows as tuples"""
    
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, email FROM users LIMIT 3")
        rows = cursor.fetchall()
        
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
            # Access by index - not very readable
```

#### **Named Row Access (sqlite3.Row)**
```python
def named_row_access():
    """Better: Use Row objects for named access"""
    
    with sqlite3.connect('database.db') as conn:
        # Configure connection to return Row objects
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, email FROM users LIMIT 3")
        rows = cursor.fetchall()
        
        for row in rows:
            # Access by column name
            print(f"ID: {row['id']}, Name: {row['name']}, Email: {row['email']}")
            
            # Also supports index access
            print(f"First column: {row[0]}")
            
            # Can convert to dictionary
            user_dict = dict(row)
            print(f"As dict: {user_dict}")
```

#### **Custom Row Factory**
```python
class User:
    """Simple User class for demonstration"""
    
    def __init__(self, id, name, email, created_at=None):
        self.id = id
        self.name = name
        self.email = email
        self.created_at = created_at
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

def user_row_factory(cursor, row):
    """Custom row factory that returns User objects"""
    
    # Get column names from cursor description
    columns = [column[0] for column in cursor.description]
    
    # Create dictionary from row
    row_dict = dict(zip(columns, row))
    
    # Return User object
    return User(**row_dict)

def custom_row_factory_example():
    """Demonstrate custom row factory"""
    
    with sqlite3.connect('database.db') as conn:
        # Set custom row factory
        conn.row_factory = user_row_factory
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, email, created_at FROM users LIMIT 3")
        users = cursor.fetchall()
        
        for user in users:
            print(user)  # Uses User.__repr__()
            print(f"User name: {user.name}")  # Access as attributes
```

---

### **Data Type Handling and Conversion**

#### **Automatic Type Conversion**
```python
import sqlite3
from datetime import datetime, date
from decimal import Decimal

def setup_type_conversion():
    """Configure automatic type conversion"""
    
    # Register adapters (Python -> SQLite)
    sqlite3.register_adapter(Decimal, str)  # Decimal -> TEXT
    sqlite3.register_adapter(datetime, lambda dt: dt.isoformat())
    
    # Register converters (SQLite -> Python)
    sqlite3.register_converter("DECIMAL", lambda s: Decimal(s.decode()))
    sqlite3.register_converter("DATETIME", lambda s: datetime.fromisoformat(s.decode()))
    
    # Connect with type parsing enabled
    conn = sqlite3.connect(
        'typed_database.db',
        detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
    )
    
    return conn

def type_conversion_example():
    """Demonstrate automatic type conversion"""
    
    conn = setup_type_conversion()
    cursor = conn.cursor()
    
    # Create table with typed columns
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            order_date DATETIME,
            total_amount DECIMAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Insert Python objects - they'll be converted automatically
    order_data = (
        datetime(2024, 1, 15, 14, 30),  # datetime object
        Decimal('123.45'),              # Decimal object
    )
    
    cursor.execute(
        "INSERT INTO orders (order_date, total_amount) VALUES (?, ?)",
        order_data
    )
    
    # Retrieve data - it's converted back to Python objects
    cursor.execute("SELECT order_date, total_amount FROM orders WHERE id = ?", 
                  (cursor.lastrowid,))
    row = cursor.fetchone()
    
    print(f"Retrieved date: {row[0]} (type: {type(row[0])})")
    print(f"Retrieved amount: {row[1]} (type: {type(row[1])})")
    
    conn.close()
```

#### **JSON Data Handling**
```python
import json

def json_adapter(obj):
    """Convert Python object to JSON string for SQLite storage"""
    return json.dumps(obj)

def json_converter(s):
    """Convert JSON string from SQLite back to Python object"""
    return json.loads(s.decode())

def json_handling_example():
    """Demonstrate JSON data storage and retrieval"""
    
    # Register JSON adapters
    sqlite3.register_adapter(dict, json_adapter)
    sqlite3.register_adapter(list, json_adapter)
    sqlite3.register_converter("JSON", json_converter)
    
    conn = sqlite3.connect('json_database.db', 
                          detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    
    # Create table with JSON column
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            metadata JSON
        )
    """)
    
    # Insert Python dict/list - converted to JSON automatically
    product_metadata = {
        'brand': 'TechCorp',
        'specs': ['16GB RAM', '512GB SSD', 'Intel i7'],
        'ratings': {'performance': 4.5, 'value': 4.0}
    }
    
    cursor.execute(
        "INSERT INTO products (name, metadata) VALUES (?, ?)",
        ('Gaming Laptop', product_metadata)
    )
    
    # Retrieve data - JSON converted back to Python dict
    cursor.execute("SELECT name, metadata FROM products WHERE id = ?",
                  (cursor.lastrowid,))
    row = cursor.fetchone()
    
    print(f"Product: {row[0]}")
    print(f"Metadata: {row[1]} (type: {type(row[1])})")
    print(f"Brand: {row[1]['brand']}")
    print(f"Specs: {row[1]['specs']}")
    
    conn.close()
```

---

### **Transaction Management**

#### **Manual Transaction Control**
```python
def manual_transaction_example():
    """Demonstrate manual transaction management"""
    
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    
    try:
        # Create test table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                name TEXT,
                balance REAL
            )
        """)
        
        # Insert initial data
        cursor.executemany(
            "INSERT OR IGNORE INTO accounts (id, name, balance) VALUES (?, ?, ?)",
            [(1, 'Alice', 1000.0), (2, 'Bob', 500.0)]
        )
        conn.commit()
        
        print("Starting balances:")
        for row in cursor.execute("SELECT name, balance FROM accounts"):
            print(f"  {row[0]}: ${row[1]}")
        
        # Start transaction for money transfer
        cursor.execute("BEGIN TRANSACTION")
        
        # Transfer $200 from Alice to Bob
        transfer_amount = 200.0
        
        # Debit Alice's account
        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (transfer_amount, 1)
        )
        
        # Credit Bob's account  
        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (transfer_amount, 2)
        )
        
        # Check if Alice has sufficient balance
        cursor.execute("SELECT balance FROM accounts WHERE id = 1")
        alice_balance = cursor.fetchone()[0]
        
        if alice_balance < 0:
            print("Insufficient funds! Rolling back transaction.")
            cursor.execute("ROLLBACK")
        else:
            print("Transfer successful! Committing transaction.")
            cursor.execute("COMMIT")
        
        # Display final balances
        print("Final balances:")
        for row in cursor.execute("SELECT name, balance FROM accounts"):
            print(f"  {row[0]}: ${row[1]}")
            
    except Exception as e:
        print(f"Error occurred: {e}")
        cursor.execute("ROLLBACK")
    finally:
        conn.close()
```

#### **Context Manager Transactions**
```python
class TransactionManager:
    """Context manager for automatic transaction handling"""
    
    def __init__(self, connection):
        self.connection = connection
        self.cursor = None
    
    def __enter__(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute("BEGIN TRANSACTION")
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            # No exception - commit transaction
            self.cursor.execute("COMMIT")
        else:
            # Exception occurred - rollback transaction
            self.cursor.execute("ROLLBACK")
            print(f"Transaction rolled back due to: {exc_val}")
        
        self.cursor.close()

def transaction_context_manager_example():
    """Using custom transaction context manager"""
    
    conn = sqlite3.connect('context_transactions.db')
    
    # Successful transaction
    try:
        with TransactionManager(conn) as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY,
                    item TEXT,
                    quantity INTEGER
                )
            """)
            
            cursor.execute(
                "INSERT INTO inventory (item, quantity) VALUES (?, ?)",
                ('Widget', 100)
            )
            
            cursor.execute(
                "UPDATE inventory SET quantity = quantity - ? WHERE item = ?",
                (10, 'Widget')
            )
            
            print("Transaction completed successfully")
            
    except Exception as e:
        print(f"Transaction failed: {e}")
    
    # Failed transaction (will rollback)
    try:
        with TransactionManager(conn) as cursor:
            cursor.execute(
                "UPDATE inventory SET quantity = quantity - ? WHERE item = ?",
                (200, 'Widget')  # This would make quantity negative
            )
            
            # Check if quantity is valid
            cursor.execute("SELECT quantity FROM inventory WHERE item = ?", ('Widget',))
            quantity = cursor.fetchone()[0]
            
            if quantity < 0:
                raise ValueError("Cannot have negative inventory")
                
    except Exception as e:
        print(f"Transaction failed and rolled back: {e}")
    
    # Verify final state
    cursor = conn.cursor()
    cursor.execute("SELECT item, quantity FROM inventory")
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]} units")
    
    conn.close()
```

---

### **Error Handling and Exception Management**

#### **SQLite Exception Hierarchy**
```python
# SQLite exception hierarchy:
# sqlite3.Error (base class)
#  ├── sqlite3.InterfaceError
#  ├── sqlite3.DatabaseError
#  │    ├── sqlite3.DataError
#  │    ├── sqlite3.OperationalError
#  │    ├── sqlite3.IntegrityError
#  │    ├── sqlite3.InternalError
#  │    ├── sqlite3.ProgrammingError
#  │    └── sqlite3.NotSupportedError

def comprehensive_error_handling():
    """Demonstrate comprehensive error handling"""
    
    try:
        conn = sqlite3.connect('error_demo.db')
        cursor = conn.cursor()
        
        # Create table with constraints
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                email TEXT UNIQUE NOT NULL,
                age INTEGER CHECK(age >= 0 AND age <= 150)
            )
        """)
        
        # Test various error conditions
        test_cases = [
            # (description, SQL, parameters, expected_exception)
            ("Constraint violation", 
             "INSERT INTO users (email, age) VALUES (?, ?)", 
             ('duplicate@email.com', 25)),
            ("Duplicate constraint violation", 
             "INSERT INTO users (email, age) VALUES (?, ?)", 
             ('duplicate@email.com', 30)),
            ("Check constraint violation", 
             "INSERT INTO users (email, age) VALUES (?, ?)", 
             ('valid@email.com', 200)),
            ("Data type error", 
             "INSERT INTO users (email, age) VALUES (?, ?)", 
             ('another@email.com', 'not_a_number')),
        ]
        
        for description, sql, params in test_cases:
            try:
                cursor.execute(sql, params)
                conn.commit()
                print(f"✅ {description}: Success")
                
            except sqlite3.IntegrityError as e:
                print(f"❌ {description}: Integrity Error - {e}")
                
            except sqlite3.DataError as e:
                print(f"❌ {description}: Data Error - {e}")
                
            except sqlite3.OperationalError as e:
                print(f"❌ {description}: Operational Error - {e}")
                
            except sqlite3.ProgrammingError as e:
                print(f"❌ {description}: Programming Error - {e}")
                
            except sqlite3.Error as e:
                print(f"❌ {description}: General SQLite Error - {e}")
        
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
    
    finally:
        if 'conn' in locals():
            conn.close()
```

#### **Robust Database Operations**
```python
import logging
from contextlib import contextmanager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@contextmanager
def robust_database_operation(db_path, max_retries=3):
    """Context manager for robust database operations with retry logic"""
    
    conn = None
    attempt = 0
    
    while attempt < max_retries:
        try:
            conn = sqlite3.connect(db_path, timeout=30.0)
            conn.execute("PRAGMA busy_timeout = 30000")  # 30 seconds
            yield conn
            break
            
        except sqlite3.OperationalError as e:
            attempt += 1
            if "database is locked" in str(e).lower() and attempt < max_retries:
                logger.warning(f"Database locked, retry {attempt}/{max_retries}")
                time.sleep(0.1 * (2 ** attempt))  # Exponential backoff
                continue
            else:
                logger.error(f"Database operation failed: {e}")
                raise
                
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
            
        finally:
            if conn:
                conn.close()

def robust_operation_example():
    """Example using robust database operations"""
    
    try:
        with robust_database_operation('busy_database.db') as conn:
            cursor = conn.cursor()
            
            cursor.execute("SELECT COUNT(*) FROM users")
            count = cursor.fetchone()[0]
            print(f"User count: {count}")
            
    except sqlite3.Error as e:
        print(f"Database operation failed after retries: {e}")
```

---

### **Advanced Features and Optimization**

#### **User-Defined Functions**
```python
import math

def create_custom_functions(conn):
    """Register custom SQL functions"""
    
    # Simple function
    def python_len(text):
        """Get length of text (similar to LENGTH() but in Python)"""
        return len(text) if text else 0
    
    # Math function
    def calculate_distance(lat1, lon1, lat2, lon2):
        """Calculate distance between two points (Haversine formula)"""
        if not all([lat1, lon1, lat2, lon2]):
            return None
            
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = (math.sin(dlat/2)**2 + 
             math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2)
        c = 2 * math.asin(math.sqrt(a))
        r = 6371  # Earth's radius in kilometers
        
        return c * r
    
    # Aggregate function
    class StdDev:
        """Custom aggregate function for standard deviation"""
        
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
    
    # Register functions
    conn.create_function("PYTHON_LEN", 1, python_len)
    conn.create_function("DISTANCE", 4, calculate_distance)
    conn.create_aggregate("STDDEV", 1, StdDev)

def custom_functions_example():
    """Demonstrate custom SQL functions"""
    
    conn = sqlite3.connect(':memory:')
    create_custom_functions(conn)
    
    cursor = conn.cursor()
    
    # Create test data
    cursor.execute("""
        CREATE TABLE locations (
            name TEXT,
            latitude REAL,
            longitude REAL,
            description TEXT
        )
    """)
    
    locations_data = [
        ('New York', 40.7128, -74.0060, 'The Big Apple'),
        ('London', 51.5074, -0.1278, 'Capital of England'),
        ('Tokyo', 35.6762, 139.6503, 'Capital of Japan'),
        ('Sydney', -33.8688, 151.2093, 'Harbor City')
    ]
    
    cursor.executemany(
        "INSERT INTO locations VALUES (?, ?, ?, ?)",
        locations_data
    )
    
    # Use custom functions
    print("Custom function examples:")
    
    # String length function
    cursor.execute("SELECT name, PYTHON_LEN(description) FROM locations")
    print("\nDescription lengths:")
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]} characters")
    
    # Distance calculation
    ny_coords = (40.7128, -74.0060)  # New York
    cursor.execute("""
        SELECT name, DISTANCE(?, ?, latitude, longitude) as distance_km
        FROM locations 
        WHERE name != 'New York'
        ORDER BY distance_km
    """, ny_coords)
    
    print(f"\nDistances from New York:")
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]:.0f} km")
    
    conn.close()
```

---

### **Performance Optimization Techniques**

#### **Connection Optimization**
```python
def optimize_connection(conn):
    """Apply comprehensive performance optimizations"""
    
    optimizations = [
        # Journal mode - WAL is fastest for concurrent access
        ("PRAGMA journal_mode = WAL", "Enable Write-Ahead Logging"),
        
        # Synchronization - NORMAL balances safety and speed
        ("PRAGMA synchronous = NORMAL", "Optimize synchronization"),
        
        # Cache size - Larger cache = better performance
        ("PRAGMA cache_size = 10000", "Set cache to ~40MB"),
        
        # Memory-mapped I/O - Faster for large databases
        ("PRAGMA mmap_size = 268435456", "Enable 256MB memory mapping"),
        
        # Temporary storage in memory
        ("PRAGMA temp_store = MEMORY", "Store temp tables in memory"),
        
        # Optimize page size for SSD
        ("PRAGMA page_size = 4096", "Set 4KB page size"),
        
        # Enable foreign key constraints
        ("PRAGMA foreign_keys = ON", "Enable foreign key constraints"),
    ]
    
    for pragma, description in optimizations:
        try:
            conn.execute(pragma)
            print(f"✅ {description}")
        except sqlite3.Error as e:
            print(f"❌ Failed to apply {description}: {e}")
    
    return conn
```

#### **Query Optimization**
```python
def query_optimization_examples():
    """Demonstrate query optimization techniques"""
    
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create table with indexes
    cursor.execute("""
        CREATE TABLE sales (
            id INTEGER PRIMARY KEY,
            product_id INTEGER,
            customer_id INTEGER,
            sale_date DATE,
            amount REAL,
            region TEXT
        )
    """)
    
    # Create indexes for common queries
    indexes = [
        "CREATE INDEX idx_sales_product ON sales(product_id)",
        "CREATE INDEX idx_sales_customer ON sales(customer_id)", 
        "CREATE INDEX idx_sales_date ON sales(sale_date)",
        "CREATE INDEX idx_sales_region ON sales(region)",
        "CREATE INDEX idx_sales_amount ON sales(amount)",
        # Composite index for complex queries
        "CREATE INDEX idx_sales_region_date ON sales(region, sale_date)"
    ]
    
    for index_sql in indexes:
        cursor.execute(index_sql)
    
    print("✅ Created optimized indexes")
    
    # Insert sample data
    import random
    from datetime import date, timedelta
    
    sample_data = []
    regions = ['North', 'South', 'East', 'West']
    start_date = date(2024, 1, 1)
    
    for i in range(10000):
        sample_data.append((
            random.randint(1, 100),  # product_id
            random.randint(1, 1000), # customer_id
            start_date + timedelta(days=random.randint(0, 365)),
            round(random.uniform(10, 1000), 2),  # amount
            random.choice(regions)
        ))
    
    cursor.executemany(
        "INSERT INTO sales (product_id, customer_id, sale_date, amount, region) VALUES (?, ?, ?, ?, ?)",
        sample_data
    )
    
    print(f"✅ Inserted {len(sample_data)} sample records")
    
    # Demonstrate query performance analysis
    cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM sales WHERE region = 'North' AND sale_date > '2024-06-01'")
    
    print("\nQuery execution plan:")
    for row in cursor.fetchall():
        print(f"  {row}")
    
    conn.close()
```

---

### **Preparation for Lab Exercise**

In the next lab, you'll implement:

1. **Connection Management**: Different connection patterns and configurations
2. **Error Handling**: Comprehensive exception handling strategies  
3. **Data Types**: Custom type conversion and JSON handling
4. **Transactions**: Manual and automatic transaction management
5. **Performance**: Query optimization and benchmarking
6. **Custom Functions**: User-defined SQL functions and aggregates

**Next Up**: Hands-on lab implementing these SQLite fundamentals!