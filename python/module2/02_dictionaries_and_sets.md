# Dictionaries and Sets in Python

## Dictionaries
Dictionaries are versatile key-value pair data structures that allow fast lookups and flexible data organization.

### Creating Dictionaries
```python
# Empty dictionary
empty_dict = {}

# Dictionary with key-value pairs
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Alternative creation method
student = dict(name="Alice", grade="A", id=12345)
```

### Basic Dictionary Operations
```python
# Accessing values
person = {"name": "John", "age": 30}
name = person["name"]  # Using key
age = person.get("age")  # Using get() method
unknown = person.get("address", "Not Found")  # With default value

# Adding/Modifying items
person["email"] = "john@example.com"  # Add new key-value pair
person["age"] = 31  # Modify existing value

# Removing items
del person["age"]  # Remove specific key
email = person.pop("email")  # Remove and return value
last_item = person.popitem()  # Remove and return last item
```

### Useful Dictionary Methods
```python
# Get all keys, values, or items
keys = person.keys()
values = person.values()
items = person.items()

# Check if key exists
has_name = "name" in person

# Update dictionary
person.update({"phone": "123-456-7890", "age": 32})

# Clear dictionary
person.clear()
```

### Dictionary Comprehension
```python
# Create dictionary from two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
student_scores = {name: score for name, score in zip(names, scores)}

# Filter and transform
passing_scores = {name: score for name, score in student_scores.items() 
                 if score >= 80}
```

## Sets
Sets are unordered collections of unique elements, perfect for removing duplicates and set operations.

### Creating Sets
```python
# Empty set (note: {} creates empty dict)
empty_set = set()

# Set from list
numbers = set([1, 2, 3, 2, 1])  # {1, 2, 3}

# Set literal
fruits = {"apple", "banana", "orange"}
```

### Set Operations
```python
# Adding and removing elements
fruits.add("mango")
fruits.remove("banana")  # Raises error if not found
fruits.discard("grape")  # No error if not found

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2  # or set1.union(set2)
intersection = set1 & set2  # or set1.intersection(set2)
difference = set1 - set2  # or set1.difference(set2)
symmetric_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
```

### Set Methods
```python
# Check membership
is_present = "apple" in fruits

# Update sets
set1.update(set2)  # Add elements from set2
set1.intersection_update(set2)  # Keep only common elements

# Check subset/superset
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)
```

## Practical Example: Student Course Management
```python
# Using both dictionaries and sets for a course management system
class CourseManager:
    def __init__(self):
        self.courses = {}  # Dictionary to store course info
        self.student_enrollments = {}  # Dictionary of sets

    def add_course(self, course_id, course_name, max_capacity):
        self.courses[course_id] = {
            "name": course_name,
            "capacity": max_capacity,
            "enrolled": 0
        }
        self.student_enrollments[course_id] = set()

    def enroll_student(self, student_id, course_id):
        if course_id not in self.courses:
            return "Course not found"
        
        if self.courses[course_id]["enrolled"] >= self.courses[course_id]["capacity"]:
            return "Course is full"
        
        self.student_enrollments[course_id].add(student_id)
        self.courses[course_id]["enrolled"] += 1
        return "Enrollment successful"

    def get_student_courses(self, student_id):
        return {course_id for course_id in self.student_enrollments 
                if student_id in self.student_enrollments[course_id]}

# Usage example
manager = CourseManager()
manager.add_course("CS101", "Intro to Programming", 30)
manager.add_course("CS102", "Data Structures", 25)

manager.enroll_student("S001", "CS101")
manager.enroll_student("S001", "CS102")
manager.enroll_student("S002", "CS101")

student_courses = manager.get_student_courses("S001")
```

## Practice Exercise
Create a program that:
1. Maintains a contact book using a dictionary
2. For each contact, store multiple phone numbers using a set
3. Implement functions to:
   - Add/remove contacts
   - Add/remove phone numbers for a contact
   - Search contacts by name or phone number
   - Display all contacts with their phone numbers
