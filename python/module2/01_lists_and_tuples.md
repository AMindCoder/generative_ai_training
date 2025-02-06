# Lists and Tuples in Python

## Introduction
Lists and tuples are fundamental data structures in Python used to store collections of items. While they share some similarities, they have key differences in terms of mutability and usage.

## Lists
Lists are mutable sequences that can store multiple items of different types.

### Creating Lists
```python
# Empty list
empty_list = []

# List with elements
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
```

### Basic List Operations
```python
# Accessing elements (0-based indexing)
numbers = [10, 20, 30, 40, 50]
first_element = numbers[0]  # 10
last_element = numbers[-1]  # 50

# Modifying elements
numbers[0] = 15

# Adding elements
numbers.append(60)  # Adds to end
numbers.insert(1, 25)  # Inserts at specific position

# Removing elements
numbers.remove(30)  # Removes first occurrence of 30
popped_element = numbers.pop()  # Removes and returns last element
```

### List Slicing
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
subset = numbers[2:5]  # [3, 4, 5]
step_slice = numbers[::2]  # [1, 3, 5, 7, 9]
```

### Common List Methods
```python
# Length of list
my_list = [1, 2, 3]
length = len(my_list)  # 3

# Sorting
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # In-place sorting
sorted_numbers = sorted(numbers)  # Returns new sorted list

# Reversing
numbers.reverse()  # In-place reversal
```

## Tuples
Tuples are immutable sequences, meaning once created, their elements cannot be changed.

### Creating Tuples
```python
# Empty tuple
empty_tuple = ()

# Tuple with elements
coordinates = (10, 20)
single_element_tuple = (1,)  # Note the comma
```

### Working with Tuples
```python
# Accessing elements
point = (3, 4)
x = point[0]  # 3
y = point[1]  # 4

# Multiple assignment using tuple unpacking
latitude, longitude = (40.7128, -74.0060)

# Tuple methods
numbers = (1, 2, 2, 3, 2)
count_2 = numbers.count(2)  # 3
index_3 = numbers.index(3)  # 3
```

### When to Use Tuples vs Lists
- Use tuples for:
  - Immutable sequences (data that shouldn't change)
  - Return values from functions
  - Dictionary keys (when needed)
  - Data integrity

- Use lists for:
  - Collections that need to be modified
  - Dynamic data
  - When you need to add/remove elements

## Practical Example: Geographic Coordinates System
```python
# Using tuples for coordinates (immutable)
locations = [
    ("New York", (40.7128, -74.0060)),
    ("London", (51.5074, -0.1278)),
    ("Tokyo", (35.6762, 139.6503))
]

# Using list for managing locations (mutable)
def add_location(locations_list, city, coordinates):
    locations_list.append((city, coordinates))

add_location(locations, "Paris", (48.8566, 2.3522))
```

## Practice Exercise
Create a program that:
1. Stores a list of student records as tuples (name, age, grade)
2. Implements functions to:
   - Add new students
   - Calculate average grade
   - Find all students above a certain grade
