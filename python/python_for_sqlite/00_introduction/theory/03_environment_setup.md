# Module 0: Course Introduction & Setup
**Chapter 3: Development Environment Setup**

---

## Complete Environment Setup Guide

This chapter will guide you through setting up a professional development environment for Python and SQLite development. By the end, you'll have everything needed to excel in this course.

---

### **System Requirements**

#### **Minimum Requirements:**
- **Operating System**: Windows 10, macOS 10.14, or Linux (Ubuntu 18+)
- **RAM**: 4GB (8GB recommended)
- **Storage**: 2GB free space
- **Internet**: For downloading packages and resources

#### **Recommended Specifications:**
- **RAM**: 8GB or more
- **Storage**: 10GB free space (for datasets and projects)
- **Processor**: Multi-core CPU for better Jupyter performance

---

### **Step 1: Python Installation**

#### **Check Existing Python Installation:**
```bash
# Check Python version
python --version
# or
python3 --version

# Check pip version
pip --version
# or
pip3 --version
```

#### **Install Python (if needed):**

**Windows:**
1. Download from [python.org](https://python.org)
2. Run installer with "Add Python to PATH" checked
3. Verify installation in Command Prompt

**macOS:**
```bash
# Using Homebrew (recommended)
brew install python

# Or download from python.org
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

#### **Verify SQLite3 Module:**
```python
# Test in Python interpreter
import sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)
```

---

### **Step 2: Virtual Environment Setup**

#### **Why Use Virtual Environments?**
- Isolate project dependencies
- Avoid version conflicts
- Maintain clean system Python
- Easy project sharing and deployment

#### **Create Virtual Environment:**
```bash
# Navigate to your course directory
cd /path/to/your/course/folder

# Create virtual environment
python -m venv sqlite_course_env

# Activate virtual environment
# Windows:
sqlite_course_env\Scripts\activate

# macOS/Linux:
source sqlite_course_env/bin/activate
```

#### **Verify Activation:**
```bash
# Your prompt should show (sqlite_course_env)
# Check Python path
which python
# Should point to your virtual environment
```

---

### **Step 3: Required Package Installation**

#### **Core Packages:**
```bash
# Upgrade pip first
pip install --upgrade pip

# Install essential packages
pip install jupyter pandas matplotlib seaborn

# Verify installations
pip list
```

#### **Package Verification:**
```python
# Test imports in Python
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import jupyter

print("All packages installed successfully!")
```

#### **Optional but Recommended:**
```bash
# Additional useful packages
pip install numpy scipy plotly sqlalchemy
```

---

### **Step 4: Jupyter Notebook Setup**

#### **Install and Configure Jupyter:**
```bash
# Install Jupyter Lab (modern interface)
pip install jupyterlab

# Or install classic Jupyter Notebook
pip install notebook

# Start Jupyter Lab
jupyter lab

# Or start classic Notebook
jupyter notebook
```

#### **Jupyter Configuration:**
```bash
# Generate configuration file
jupyter notebook --generate-config

# Common configuration options (optional)
# Edit ~/.jupyter/jupyter_notebook_config.py
```

#### **Useful Jupyter Extensions:**
```bash
# Install useful extensions
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Enable specific extensions
jupyter nbextension enable --py widgetsnbextension
```

---

### **Step 5: Text Editor/IDE Setup**

#### **VS Code (Recommended):**
1. Download from [code.visualstudio.com](https://code.visualstudio.com)
2. Install Python extension
3. Install Jupyter extension
4. Configure Python interpreter

**Essential VS Code Extensions:**
- Python (Microsoft)
- Jupyter (Microsoft)
- SQLite Viewer
- Python Docstring Generator

#### **Alternative Editors:**
- **PyCharm**: Full-featured Python IDE
- **Sublime Text**: Lightweight with Python plugins
- **Vim/Neovim**: For advanced users
- **Atom**: GitHub's editor (deprecated but still usable)

---

### **Step 6: SQLite Tools (Optional but Helpful)**

#### **Command-Line SQLite:**
```bash
# Check if sqlite3 is available
sqlite3 --version

# If not available, install:
# Windows: Download from sqlite.org
# macOS: brew install sqlite
# Linux: sudo apt install sqlite3
```

#### **GUI Tools for SQLite:**
- **DB Browser for SQLite**: Free, cross-platform
- **SQLiteStudio**: Feature-rich, free
- **Navicat for SQLite**: Commercial, professional
- **DBeaver**: Free, multi-database support

#### **VS Code SQLite Extensions:**
- SQLite Viewer: View database files
- SQLite: Execute queries directly in VS Code

---

### **Step 7: Project Directory Structure**

#### **Recommended Directory Layout:**
```
sqlite_course/
├── 00_introduction/
├── 01_sqlite_fundamentals/
├── 02_sql_statements/
├── 03_aggregate_functions/
├── 04_pandas_integration/
├── 05_visualization/
├── 06_final_project/
├── datasets/
├── notebooks/
├── scripts/
└── resources/
```

#### **Create Directory Structure:**
```bash
# Create main course directory
mkdir sqlite_course
cd sqlite_course

# Create module directories
mkdir {00_introduction,01_sqlite_fundamentals,02_sql_statements,03_aggregate_functions,04_pandas_integration,05_visualization,06_final_project}

# Create supporting directories
mkdir {datasets,notebooks,scripts,resources}
```

---

### **Step 8: Git Setup (Recommended)**

#### **Install Git:**
- **Windows**: Download from [git-scm.com](https://git-scm.com)
- **macOS**: `brew install git` or included with Xcode
- **Linux**: `sudo apt install git`

#### **Configure Git:**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### **Initialize Repository:**
```bash
# In your course directory
git init
git add .
git commit -m "Initial course setup"
```

#### **Create .gitignore:**
```bash
# Create .gitignore file
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
.Python
env/
venv/
.venv/

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# SQLite
*.db
*.sqlite
*.sqlite3

# VS Code
.vscode/

# OS
.DS_Store
Thumbs.db
EOF
```

---

### **Step 9: Environment Testing**

#### **Complete System Test:**
Create a test file `environment_test.py`:

```python
#!/usr/bin/env python3
"""
Environment Setup Verification Script
Tests all required components for the Python SQLite course
"""

import sys
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_python_version():
    """Test Python version compatibility"""
    version = sys.version_info
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✓ Python version is compatible")
        return True
    else:
        print("✗ Python 3.8+ required")
        return False

def test_sqlite():
    """Test SQLite functionality"""
    try:
        # Create in-memory database
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        
        # Test basic operations
        cursor.execute('''CREATE TABLE test (id INTEGER, name TEXT)''')
        cursor.execute('''INSERT INTO test VALUES (1, 'Hello World')''')
        result = cursor.fetchone()
        
        conn.close()
        
        print(f"✓ SQLite {sqlite3.sqlite_version}")
        print("✓ SQLite operations working")
        return True
    except Exception as e:
        print(f"✗ SQLite error: {e}")
        return False

def test_pandas():
    """Test Pandas functionality"""
    try:
        # Create test DataFrame
        df = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})
        
        # Test SQLite integration
        conn = sqlite3.connect(':memory:')
        df.to_sql('test_table', conn, index=False)
        
        # Read back from database
        result_df = pd.read_sql('SELECT * FROM test_table', conn)
        conn.close()
        
        print(f"✓ Pandas {pd.__version__}")
        print("✓ Pandas-SQLite integration working")
        return True
    except Exception as e:
        print(f"✗ Pandas error: {e}")
        return False

def test_matplotlib():
    """Test Matplotlib functionality"""
    try:
        # Create simple plot
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot([1, 2, 3], [1, 4, 2])
        ax.set_title('Test Plot')
        
        # Don't display, just test creation
        plt.close()
        
        print(f"✓ Matplotlib {plt.__version__}")
        print("✓ Matplotlib plotting working")
        return True
    except Exception as e:
        print(f"✗ Matplotlib error: {e}")
        return False

def test_seaborn():
    """Test Seaborn functionality"""
    try:
        # Test basic seaborn functionality
        sns.set_style("whitegrid")
        
        print(f"✓ Seaborn {sns.__version__}")
        print("✓ Seaborn styling working")
        return True
    except Exception as e:
        print(f"✗ Seaborn error: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 50)
    print("PYTHON SQLITE COURSE - ENVIRONMENT TEST")
    print("=" * 50)
    
    tests = [
        test_python_version,
        test_sqlite,
        test_pandas,
        test_matplotlib,
        test_seaborn
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
            print("-" * 30)
        except Exception as e:
            print(f"✗ Unexpected error in {test.__name__}: {e}")
            results.append(False)
            print("-" * 30)
    
    print("=" * 50)
    if all(results):
        print("🎉 ALL TESTS PASSED!")
        print("Your environment is ready for the course!")
    else:
        print("❌ SOME TESTS FAILED")
        print("Please fix the issues above before continuing.")
    print("=" * 50)

if __name__ == "__main__":
    main()
```

#### **Run the Test:**
```bash
python environment_test.py
```

---

### **Step 10: Course Resources Setup**

#### **Download Course Materials:**
```bash
# Create resources directory
mkdir -p resources/sample_data

# We'll populate this with datasets in later modules
```

#### **Bookmark Important Documentation:**
- [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQLite Documentation](https://sqlite.org/docs.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [Seaborn Documentation](https://seaborn.pydata.org/)

---

### **Troubleshooting Common Issues**

#### **Python/Pip Issues:**
```bash
# Python not found
# Add Python to PATH or use full path

# Permission errors
# Use --user flag: pip install --user package_name

# Virtual environment not activating
# Check path and permissions
```

#### **Jupyter Issues:**
```bash
# Kernel not found
python -m ipykernel install --user --name=sqlite_course_env

# Port already in use
jupyter notebook --port=8889
```

#### **Import Errors:**
```bash
# Module not found
# Ensure virtual environment is activated
# Reinstall with: pip install --upgrade package_name
```

---

### **Performance Optimization Tips**

#### **Jupyter Performance:**
```python
# Add to notebook cell for better performance
%config InlineBackend.figure_format = 'retina'
%matplotlib inline

# Memory usage monitoring
%load_ext memory_profiler
%memit your_function()
```

#### **SQLite Performance:**
```python
# Connection optimization
conn = sqlite3.connect('database.db')
conn.execute('PRAGMA journal_mode=WAL')
conn.execute('PRAGMA synchronous=NORMAL')
conn.execute('PRAGMA cache_size=10000')
```

---

### **What's Next?**

Congratulations! Your development environment is now ready. In the next section, we'll create our first lab exercise where you'll:

1. Create your first SQLite database
2. Connect to it using Python
3. Perform basic operations
4. Verify everything works correctly

**Ready for your first hands-on experience? Let's move to the lab!**

---

### **Quick Reference: Activation Commands**

```bash
# Activate virtual environment
# Windows:
sqlite_course_env\Scripts\activate

# macOS/Linux:
source sqlite_course_env/bin/activate

# Start Jupyter
jupyter lab

# Deactivate when done
deactivate
```