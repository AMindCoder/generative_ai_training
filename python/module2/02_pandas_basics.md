# Pandas Basics

Pandas is a powerful Python library for data manipulation and analysis. Built on top of NumPy, it provides data structures and functions needed to efficiently work with structured data.

## Core Data Structures

Pandas has two primary data structures:

1. **Series**: A one-dimensional labeled array capable of holding any data type
2. **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types

## Creating Series and DataFrames

### Series

```python
import pandas as pd
import numpy as np

# Create a Series from a list
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64

# Create a Series with custom index
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)
# a    1
# b    2
# c    3
# d    4
# dtype: int64

# Create a Series from a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
s = pd.Series(d)
print(s)
# a    1
# b    2
# c    3
# dtype: int64
```

### DataFrame

```python
# Create a DataFrame from a dictionary of Series
d = {'col1': pd.Series([1, 2, 3]), 
     'col2': pd.Series([4, 5, 6])}
df = pd.DataFrame(d)
print(df)
#    col1  col2
# 0     1     4
# 1     2     5
# 2     3     6

# Create a DataFrame from a dictionary of lists
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)
print(df)
#     Name  Age      City
# 0   John   28  New York
# 1   Anna   24     Paris
# 2  Peter   35    Berlin
# 3  Linda   32    London

# Create a DataFrame from a 2D NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df)
#    A  B  C
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9
```

## Reading and Writing Data

Pandas can read data from various file formats:

```python
# Read CSV file
df = pd.read_csv('data.csv')

# Read Excel file
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Read JSON file
df = pd.read_json('data.json')

# Write to CSV
df.to_csv('output.csv', index=False)

# Write to Excel
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

# Write to JSON
df.to_json('output.json')
```

## Viewing Data

```python
# Display the first 5 rows
print(df.head())

# Display the last 5 rows
print(df.tail())

# Display DataFrame information
print(df.info())

# Display statistical summary
print(df.describe())

# Get dimensions
print(df.shape)  # (rows, columns)

# Get column names
print(df.columns)

# Get data types of columns
print(df.dtypes)
```

## Selecting and Filtering Data

### Selecting Columns

```python
# Select a single column (returns Series)
ages = df['Age']

# Select multiple columns (returns DataFrame)
subset = df[['Name', 'Age']]
```

### Selecting Rows

```python
# Select by position using iloc
first_row = df.iloc[0]  # First row
first_three_rows = df.iloc[0:3]  # First three rows
specific_cells = df.iloc[0:2, 1:3]  # First two rows, second and third columns

# Select by label using loc
row_by_index = df.loc[2]  # Row with index 2
subset_by_index = df.loc[1:3, ['Name', 'Age']]  # Rows 1-3, columns Name and Age
```

### Filtering

```python
# Filter rows based on a condition
adults = df[df['Age'] >= 18]

# Multiple conditions
young_adults = df[(df['Age'] >= 18) & (df['Age'] < 30)]

# Filter based on string content
new_yorkers = df[df['City'] == 'New York']

# String methods
starts_with_n = df[df['City'].str.startswith('N')]
contains_on = df[df['City'].str.contains('on')]
```

## Adding and Modifying Data

```python
# Add a new column
df['Country'] = ['USA', 'France', 'Germany', 'UK']

# Modify values
df.loc[0, 'Age'] = 29

# Apply a function to a column
df['Age'] = df['Age'].apply(lambda x: x + 1)

# Add a new row
new_row = {'Name': 'Michael', 'Age': 41, 'City': 'Toronto', 'Country': 'Canada'}
df = df.append(new_row, ignore_index=True)

# Drop columns
df_no_country = df.drop('Country', axis=1)

# Drop rows
df_no_first = df.drop(0, axis=0)
```

## Handling Missing Data

```python
# Check for missing values
print(df.isnull().sum())

# Drop rows with any missing values
df_clean = df.dropna()

# Drop rows where all values are missing
df_clean = df.dropna(how='all')

# Fill missing values with a specific value
df_filled = df.fillna(0)

# Fill missing values with different values for each column
df_filled = df.fillna({'Age': 0, 'City': 'Unknown'})

# Forward fill (use previous value)
df_filled = df.fillna(method='ffill')

# Backward fill (use next value)
df_filled = df.fillna(method='bfill')
```

## Grouping and Aggregation

```python
# Group by a column
grouped = df.groupby('City')

# Aggregate statistics
city_stats = grouped.agg({'Age': ['mean', 'min', 'max', 'count']})

# Group by multiple columns
multi_grouped = df.groupby(['Country', 'City'])

# Apply a function to each group
def age_range(x):
    return x.max() - x.min()

age_ranges = df.groupby('City')['Age'].apply(age_range)
```

## Merging and Joining DataFrames

```python
# Create two DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32]
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'City': ['New York', 'Paris', 'Berlin', 'Rome'],
    'Country': ['USA', 'France', 'Germany', 'Italy']
})

# Inner join (only matching keys)
merged_inner = pd.merge(df1, df2, on='ID', how='inner')

# Left join (all keys from left DataFrame)
merged_left = pd.merge(df1, df2, on='ID', how='left')

# Right join (all keys from right DataFrame)
merged_right = pd.merge(df1, df2, on='ID', how='right')

# Outer join (all keys from both DataFrames)
merged_outer = pd.merge(df1, df2, on='ID', how='outer')

# Concatenate DataFrames vertically
concatenated = pd.concat([df1, df1], ignore_index=True)
```

## Reshaping Data

```python
# Pivot table
pivot = df.pivot_table(values='Age', index='Country', columns='City', aggfunc='mean')

# Melt (unpivot) - convert from wide to long format
melted = pd.melt(df, id_vars=['Name'], value_vars=['Age', 'Height'])

# Stack and unstack
stacked = df.stack()  # Pivots columns to rows
unstacked = stacked.unstack()  # Pivots rows to columns
```

## Time Series Data

```python
# Create a date range
dates = pd.date_range('20230101', periods=6)

# Create a DataFrame with dates as index
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

# Resample time series data
monthly = df.resample('M').mean()  # Monthly average

# Shift data
shifted = df.shift(1)  # Shift values by 1 period

# Rolling statistics
rolling_mean = df.rolling(window=3).mean()
```

## Conclusion

Pandas is an essential tool for data manipulation and analysis in Python. Its rich functionality for handling structured data makes it indispensable for data scientists and analysts. Understanding Pandas is a crucial step in the data processing pipeline before moving on to data visualization and machine learning.
