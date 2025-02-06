**Module 1: Introduction to Python**  
**Chapter 3: Variables & Data Types**  

---

### **1. Understanding Variables in Python**  
Variables are fundamental building blocks in Python, acting as containers for data. In machine learning, they're crucial for storing everything from simple numbers to complex neural network parameters.

#### **Variable Naming Rules**
```python
# Valid variable names
model_accuracy = 95.5
numberOfEpochs = 100
X_train = [1, 2, 3, 4]

# Invalid variable names
2nd_model = "CNN"    # Can't start with number
class = "classifier" # Can't use Python keywords
```

### **2. Core Data Types for ML**

#### **1. Numeric Types**
```python
# Integer (int) - Whole numbers
batch_size = 32
num_classes = 10

# Float (float) - Decimal numbers
learning_rate = 0.001
model_accuracy = 98.75

# Complex numbers (complex) - Used in signal processing
signal = 3 + 4j
```

#### **2. Text Type**
```python
# String (str) - Text data
model_name = "Neural Network"
dataset_path = "data/training/"

# String operations crucial for data preprocessing
text = "Machine Learning"
print(text.lower())        # machine learning
print(text.split())        # ['Machine', 'Learning']
```

#### **3. Boolean Type**
```python
# Boolean (bool) - True/False
is_trained = True
has_gpu = False

# Boolean operations
is_ready = is_trained and has_gpu
```

### **3. Collections - Complex Data Types**

#### **1. Lists**
```python
# Lists - Ordered, mutable sequences
features = [1.2, 3.4, 5.6, 7.8]
labels = ['cat', 'dog', 'bird']

# List operations
features.append(9.0)       # Add element
print(features[0])        # Access first element
print(features[-1])       # Access last element
```

#### **2. Tuples**
```python
# Tuples - Ordered, immutable sequences
model_config = (128, 64, 32)  # Layer sizes
image_shape = (224, 224, 3)   # Height, width, channels
```

#### **3. Sets**
```python
# Sets - Unordered collection of unique elements
unique_labels = {'positive', 'negative', 'neutral'}
unique_features = {1, 2, 3, 3, 2, 1}  # Duplicates removed automatically
```

#### **4. Dictionaries**
```python
# Dictionaries - Key-value pairs
model_params = {
    'learning_rate': 0.001,
    'epochs': 100,
    'batch_size': 32
}
```

### **4. Type Conversion**
```python
# Converting between types
accuracy = float('98.5')           # String to float
batch_size = int(32.9)            # Float to int
feature_list = list((1, 2, 3))    # Tuple to list

# Type checking
print(type(accuracy))             # <class 'float'>
print(isinstance(batch_size, int)) # True
```

### **5. Special Types in Data Science**
```python
import numpy as np

# NumPy arrays - Foundation for ML
array_1d = np.array([1, 2, 3])              # 1D array
array_2d = np.array([[1, 2], [3, 4]])       # 2D array (matrix)

# Data types in NumPy
float_array = np.array([1, 2, 3], dtype=np.float32)
int_array = np.array([1, 2, 3], dtype=np.int64)
```

### **Practice Exercise**
1. Create variables to store different aspects of a neural network (layers, activation functions, etc.)
2. Practice type conversion between different numeric types
3. Create a dictionary to store model hyperparameters
4. Work with lists to store training data and labels

### **Key Takeaways**
- Understanding data types is crucial for efficient memory usage in ML
- Python's dynamic typing allows flexibility but requires careful type checking
- Complex data types (lists, dictionaries) are fundamental for organizing ML data
- NumPy introduces specialized types for efficient numerical computations
