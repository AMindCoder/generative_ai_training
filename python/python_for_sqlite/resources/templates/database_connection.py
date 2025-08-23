"""Database Connection Template

Reusable database connection and management utilities for SQLite projects.
"""

import sqlite3
import json
from contextlib import contextmanager
from decimal import Decimal
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseManager:
    """Professional database management class for SQLite operations"""
    
    def __init__(self, db_path, **kwargs):
        self.db_path = db_path
        self.connection = None
        self.config = {
            'timeout': 30.0,
            'detect_types': sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
            'check_same_thread': False,
            **kwargs
        }
        
        # Register custom type adapters
        self._register_adapters()
    
    def _register_adapters(self):
        """Register custom type adapters and converters"""
        
        # JSON adapter/converter
        sqlite3.register_adapter(dict, lambda d: json.dumps(d))
        sqlite3.register_adapter(list, lambda l: json.dumps(l))
        sqlite3.register_converter("JSON", lambda s: json.loads(s.decode()))
        
        # Decimal adapter/converter
        sqlite3.register_adapter(Decimal, str)
        sqlite3.register_converter("DECIMAL", lambda s: Decimal(s.decode()))
        
        # Boolean adapter/converter
        sqlite3.register_adapter(bool, int)
        sqlite3.register_converter("BOOLEAN", lambda s: bool(int(s)))
    
    def connect(self):
        """Establish optimized database connection"""
        
        try:
            self.connection = sqlite3.connect(self.db_path, **self.config)
            
            # Set row factory for named access
            self.connection.row_factory = sqlite3.Row
            
            # Apply performance optimizations
            self._optimize_connection()
            
            logger.info(f"Connected to database: {self.db_path}")
            return self.connection
            
        except sqlite3.Error as e:
            logger.error(f"Failed to connect to database: {e}")
            raise
    
    def _optimize_connection(self):
        """Apply performance optimizations"""
        
        optimizations = [
            "PRAGMA foreign_keys = ON",
            "PRAGMA journal_mode = WAL",
            "PRAGMA synchronous = NORMAL",
            "PRAGMA cache_size = 10000",
            "PRAGMA temp_store = MEMORY"
        ]
        
        for pragma in optimizations:
            try:
                self.connection.execute(pragma)
            except sqlite3.Error as e:
                logger.warning(f"Failed to apply optimization '{pragma}': {e}")
    
    @contextmanager
    def get_cursor(self):
        """Context manager for cursor operations"""
        if not self.connection:
            self.connect()
        
        cursor = self.connection.cursor()
        try:
            yield cursor
        finally:
            cursor.close()
    
    @contextmanager
    def transaction(self):
        """Context manager for automatic transaction handling"""
        cursor = self.connection.cursor() if self.connection else None
        
        if not cursor:
            raise RuntimeError("No database connection available")
        
        try:
            cursor.execute("BEGIN TRANSACTION")
            yield cursor
            cursor.execute("COMMIT")
            logger.debug("Transaction committed successfully")
            
        except Exception as e:
            cursor.execute("ROLLBACK")
            logger.error(f"Transaction rolled back: {e}")
            raise
        
        finally:
            cursor.close()
    
    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            self.connection = None
            logger.info("Database connection closed")
    
    def __enter__(self):
        """Context manager entry"""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()


# Example usage
if __name__ == "__main__":
    
    # Using context manager
    with DatabaseManager('example.db') as db:
        
        # Create sample table
        with db.get_cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sample (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    data JSON,
                    amount DECIMAL(10,2),
                    is_active BOOLEAN DEFAULT 1
                )
            """)
        
        # Insert sample data using transaction
        with db.transaction() as cursor:
            sample_data = {
                'type': 'example',
                'values': [1, 2, 3]
            }
            
            cursor.execute("""
                INSERT INTO sample (name, data, amount, is_active)
                VALUES (?, ?, ?, ?)
            """, ('Test Record', sample_data, Decimal('99.99'), True))
        
        print("Sample database operations completed successfully!")