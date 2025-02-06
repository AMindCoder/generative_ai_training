# String Manipulation and Regular Expressions in Python

## String Basics and Manipulation

### String Creation and Basic Operations
```python
# String creation
single_quoted = 'Hello'
double_quoted = "World"
multi_line = '''This is a
multi-line string'''

# String concatenation
greeting = single_quoted + ' ' + double_quoted  # 'Hello World'
repeated = 'Ha' * 3  # 'HaHaHa'

# String length
length = len(greeting)  # 11
```

### String Indexing and Slicing
```python
text = "Python Programming"

# Indexing (0-based)
first_char = text[0]       # 'P'
last_char = text[-1]       # 'g'

# Slicing [start:end:step]
first_word = text[0:6]     # 'Python'
last_word = text[7:]       # 'Programming'
reverse = text[::-1]       # 'gnimmargorP nohtyP'
every_second = text[::2]   # 'Pto rgamn'
```

### String Methods for Text Processing
```python
text = "  Python Programming Is Fun!  "

# Case manipulation
upper_case = text.upper()          # "  PYTHON PROGRAMMING IS FUN!  "
lower_case = text.lower()          # "  python programming is fun!  "
title_case = text.title()          # "  Python Programming Is Fun!  "
swapped_case = text.swapcase()     # "  pYTHON pROGRAMMING iS fUN!  "

# Whitespace handling
stripped = text.strip()            # "Python Programming Is Fun!"
left_stripped = text.lstrip()      # "Python Programming Is Fun!  "
right_stripped = text.rstrip()     # "  Python Programming Is Fun!"

# Finding and counting
count_m = text.count('m')          # 2
find_prog = text.find('Program')   # 8 (returns -1 if not found)
index_is = text.index('Is')        # 18 (raises ValueError if not found)

# Checking string properties
is_alpha = "Hello123".isalpha()    # False
is_digit = "123".isdigit()         # True
is_alnum = "Hello123".isalnum()    # True
is_space = "   ".isspace()         # True
```

### String Formatting Methods
```python
name = "Alice"
age = 25
height = 1.75

# %-formatting (old style)
old_style = "Name: %s, Age: %d, Height: %.2f" % (name, age, height)

# str.format() method
format_style = "Name: {}, Age: {}, Height: {:.2f}".format(name, age, height)

# f-strings (Python 3.6+)
f_string = f"Name: {name}, Age: {age}, Height: {height:.2f}"

# Format specifiers
price = 1234.5678
formatted_price = f"Price: ${price:,.2f}"  # "Price: $1,234.57"

# Alignment and padding
left_aligned = f"|{name:<10}|"    # |Alice     |
right_aligned = f"|{name:>10}|"   # |     Alice|
center_aligned = f"|{name:^10}|"  # |  Alice   |
zero_padded = f"{42:05d}"         # "00042"
```

### String Split and Join Operations
```python
# Splitting strings
sentence = "Python is a great language"
words = sentence.split()           # ['Python', 'is', 'a', 'great', 'language']
csv_data = "apple,banana,orange"
fruits = csv_data.split(',')       # ['apple', 'banana', 'orange']

# Joining strings
joined_words = ' '.join(words)     # "Python is a great language"
joined_fruits = ', '.join(fruits)  # "apple, banana, orange"

# Splitting with maximum splits
limited_split = sentence.split(' ', 2)  # ['Python', 'is', 'a great language']
```

## Regular Expressions (re package)
Regular expressions provide powerful pattern matching and text manipulation capabilities.

### Basic Pattern Matching
```python
import re

text = "Contact us at: support@example.com or sales@example.com"

# Finding all email addresses
email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
emails = re.findall(email_pattern, text)
# ['support@example.com', 'sales@example.com']

# Checking if pattern exists
has_email = re.search(email_pattern, text) is not None  # True
```

### Common Regular Expression Patterns
```python
# Phone number patterns
phone_text = "Call us: 123-456-7890 or (987) 654-3210"
phone_patterns = [
    r'\d{3}-\d{3}-\d{4}',         # 123-456-7890
    r'\(\d{3}\)\s\d{3}-\d{4}'     # (987) 654-3210
]

for pattern in phone_patterns:
    matches = re.findall(pattern, phone_text)
    print(f"Pattern {pattern}: {matches}")

# Date patterns
date_text = "Dates: 2023-12-31, 01/15/2024, 15-Jan-2024"
date_patterns = [
    r'\d{4}-\d{2}-\d{2}',         # YYYY-MM-DD
    r'\d{2}/\d{2}/\d{4}',         # MM/DD/YYYY
    r'\d{2}-[A-Za-z]{3}-\d{4}'    # DD-Mon-YYYY
]

for pattern in date_patterns:
    matches = re.findall(pattern, date_text)
    print(f"Pattern {pattern}: {matches}")
```

### Advanced Regular Expression Operations
```python
# Pattern substitution
text = "My SSN is 123-45-6789 and credit card is 1234-5678-9012-3456"

# Hide sensitive information
hidden_ssn = re.sub(r'\d{3}-\d{2}-\d{4}', 'XXX-XX-XXXX', text)
hidden_card = re.sub(r'\d{4}-\d{4}-\d{4}-\d{4}', 'XXXX-XXXX-XXXX-XXXX', hidden_ssn)

# Pattern groups
log_entry = "2024-02-06 14:30:45 - User 'admin' logged in"
pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) - User \'(\w+)\' (\w+ \w+)'

match = re.search(pattern, log_entry)
if match:
    date, time, user, action = match.groups()
    print(f"Date: {date}, Time: {time}, User: {user}, Action: {action}")
```

## Practical Example: Text Analysis Tool
```python
import re
from collections import Counter

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.words = re.findall(r'\b\w+\b', text.lower())
        
    def word_frequency(self):
        return Counter(self.words)
    
    def find_emails(self):
        pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
        return re.findall(pattern, self.text)
    
    def find_urls(self):
        pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
        return re.findall(pattern, self.text)
    
    def replace_sensitive_info(self):
        # Replace email addresses
        text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '[EMAIL]', self.text)
        # Replace phone numbers
        text = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[PHONE]', text)
        return text

# Usage example
sample_text = """
Contact John Doe at john.doe@example.com or visit https://example.com
Phone: 123-456-7890
Alternative email: support@company.com
"""

analyzer = TextAnalyzer(sample_text)
print("Word Frequencies:", analyzer.word_frequency())
print("Emails:", analyzer.find_emails())
print("URLs:", analyzer.find_urls())
print("Redacted Text:", analyzer.replace_sensitive_info())
```

## Practice Exercise
Create a program that:
1. Reads a text file containing customer data
2. Extracts and validates:
   - Email addresses
   - Phone numbers
   - Postal codes
   - Dates in various formats
3. Generates a report showing:
   - Valid vs invalid data entries
   - Statistics about data formats used
   - Suggestions for standardizing the data format
