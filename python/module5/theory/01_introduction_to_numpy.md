# Introduction to NumPy

NumPy (Numerical Python) is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

## Why NumPy?

- **Performance**: NumPy operations are executed in pre-compiled C code, making them much faster than Python loops
- **Memory Efficiency**: NumPy arrays are more compact than Python lists
- **Convenience**: NumPy offers many built-in functions for common array operations
- **Foundation**: Many scientific and data analysis libraries (like Pandas, SciPy, scikit-learn) are built on NumPy

## NumPy Arrays

The core of NumPy is the `ndarray` (N-dimensional array) object:

```python
import numpy as np

# Creating arrays
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Array attributes
print(f"Shape: {array_2d.shape}")  # (2, 3)
print(f"Dimensions: {array_2d.ndim}")  # 2
print(f"Data type: {array_2d.dtype}")  # int64
print(f"Size: {array_2d.size}")  # 6
```

## Array Creation Functions

NumPy provides various functions to create arrays:

```python
# Create array of zeros
zeros = np.zeros((3, 4))

# Create array of ones
ones = np.ones((2, 3, 4))

# Create array with a range of values
range_array = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Create evenly spaced values within a range
linspace = np.linspace(0, 1, 5)  # [0., 0.25, 0.5, 0.75, 1.]

# Create identity matrix
identity = np.eye(3)

# Create array with random values
random_array = np.random.random((2, 2))
```

## Array Indexing and Slicing

NumPy arrays can be indexed and sliced similar to Python lists, but with extended capabilities for multi-dimensional arrays:

```python
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Indexing
print(array_2d[0, 0])  # 1
print(array_2d[2, 3])  # 12

# Slicing
print(array_2d[0:2, 1:3])  # [[2, 3], [6, 7]]

# Boolean indexing
mask = array_2d > 5
print(array_2d[mask])  # [6, 7, 8, 9, 10, 11, 12]
```

## Array Operations

NumPy provides vectorized operations that work element-wise on arrays:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Arithmetic operations
print(a + b)  # [5, 7, 9]
print(a * b)  # [4, 10, 18]
print(a ** 2)  # [1, 4, 9]

# Statistical operations
print(np.mean(a))  # 2.0
print(np.sum(a))   # 6
print(np.max(b))   # 6
print(np.min(b))   # 4
print(np.std(a))   # 0.816...

# Linear algebra
c = np.array([[1, 2], [3, 4]])
d = np.array([[5, 6], [7, 8]])
print(np.dot(c, d))  # Matrix multiplication: [[19, 22], [43, 50]]
```

## Broadcasting

Broadcasting is a powerful mechanism that allows NumPy to work with arrays of different shapes:

```python
# Add a scalar to an array
a = np.array([1, 2, 3])
print(a + 10)  # [11, 12, 13]

# Add a 1D array to a 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([10, 20, 30])
print(b + c)  # [[11, 22, 33], [14, 25, 36]]
```

## Reshaping Arrays

NumPy provides functions to change the shape of arrays:

```python
a = np.arange(12)
print(a)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Reshape to 2D array
b = a.reshape(3, 4)
print(b)
# [[ 0,  1,  2,  3],
#  [ 4,  5,  6,  7],
#  [ 8,  9, 10, 11]]

# Transpose
print(b.T)
# [[ 0,  4,  8],
#  [ 1,  5,  9],
#  [ 2,  6, 10],
#  [ 3,  7, 11]]

# Flatten array
print(b.flatten())  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

## Conclusion

NumPy is an essential library for data processing in Python. Its efficient array operations and mathematical functions make it the foundation for data analysis and scientific computing. Understanding NumPy is crucial before moving on to higher-level libraries like Pandas and Matplotlib.
