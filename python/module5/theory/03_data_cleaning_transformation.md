# Data Cleaning and Transformation

Data cleaning and transformation are critical steps in the data processing pipeline. Real-world data is often messy, incomplete, and not immediately suitable for analysis. This module covers essential techniques for preparing your data for analysis.

## Common Data Quality Issues

1. **Missing values**: Empty cells or placeholder values like 'N/A', 'Unknown', etc.
2. **Duplicates**: Identical or nearly identical records
3. **Inconsistent formatting**: Different date formats, capitalization, etc.
4. **Outliers**: Values that significantly deviate from the norm
5. **Data type issues**: Numbers stored as strings, etc.
6. **Structural problems**: Denormalized data, nested data, etc.

## Handling Missing Values

```python
import pandas as pd
import numpy as np

# Create a DataFrame with missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})

# Identify missing values
print(df.isnull())  # Returns boolean mask
print(df.isnull().sum())  # Count missing values per column
print(df.isnull().sum().sum())  # Total missing values

# Drop rows with any missing values
df_dropped = df.dropna()

# Drop rows where all values are missing
df_dropped_all = df.dropna(how='all')

# Drop columns with missing values
df_dropped_cols = df.dropna(axis=1)

# Fill missing values with a constant
df_filled = df.fillna(0)

# Fill with column mean
df_filled_mean = df.fillna(df.mean())

# Fill with column median
df_filled_median = df.fillna(df.median())

# Forward fill (propagate last valid observation forward)
df_ffill = df.fillna(method='ffill')

# Backward fill (use next valid observation to fill gap)
df_bfill = df.fillna(method='bfill')

# Interpolate missing values
df_interp = df.interpolate()
```

## Handling Duplicates

```python
# Create a DataFrame with duplicates
df = pd.DataFrame({
    'A': [1, 2, 2, 3, 3],
    'B': [5, 6, 6, 7, 8]
})

# Identify duplicates
print(df.duplicated())  # Returns boolean Series
print(df.duplicated().sum())  # Count duplicates

# Drop exact duplicates
df_unique = df.drop_duplicates()

# Drop duplicates based on specific columns
df_unique_cols = df.drop_duplicates(subset=['A'])

# Keep first or last occurrence
df_unique_last = df.drop_duplicates(keep='last')
```

## Data Type Conversion

```python
# Create a DataFrame with mixed types
df = pd.DataFrame({
    'A': ['1', '2', '3', '4'],
    'B': [5, 6, 7, 8],
    'C': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04']
})

# Check data types
print(df.dtypes)

# Convert string to numeric
df['A'] = pd.to_numeric(df['A'])

# Convert to datetime
df['C'] = pd.to_datetime(df['C'])

# Convert multiple columns at once
df = df.astype({'A': 'int', 'B': 'float'})

# Handle errors in conversion
df['A'] = pd.to_numeric(df['A'], errors='coerce')  # Invalid values become NaN
```

## String Manipulation

```python
# Create a DataFrame with string data
df = pd.DataFrame({
    'Name': ['John Smith', 'Jane Doe', 'Bob Johnson', 'Sarah Williams'],
    'Email': ['john.smith@example.com', 'jane.doe@example.com', 
              'bob.johnson@example.com', 'sarah.williams@example.com']
})

# Access string methods
df['Name'] = df['Name'].str.upper()  # Convert to uppercase
df['Name'] = df['Name'].str.lower()  # Convert to lowercase
df['Name'] = df['Name'].str.title()  # Title case

# Split strings
df['First_Name'] = df['Name'].str.split(' ').str[0]
df['Last_Name'] = df['Name'].str.split(' ').str[1]

# Extract patterns
df['Domain'] = df['Email'].str.extract(r'@(.+)$')

# Replace patterns
df['Name'] = df['Name'].str.replace('John', 'Jonathan')

# Strip whitespace
df['Name'] = df['Name'].str.strip()

# Check if string contains pattern
mask = df['Email'].str.contains('example.com')
```

## Handling Outliers

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame with outliers
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 100]  # 100 is an outlier
})

# Visualize to identify outliers
plt.boxplot(df['A'])
plt.show()

# Z-score method
from scipy import stats
z_scores = stats.zscore(df['A'])
abs_z_scores = abs(z_scores)
filtered_entries = (abs_z_scores < 3)  # Keep only values with z-score < 3
df_no_outliers = df[filtered_entries]

# IQR method
Q1 = df['A'].quantile(0.25)
Q3 = df['A'].quantile(0.75)
IQR = Q3 - Q1
df_no_outliers = df[(df['A'] >= Q1 - 1.5 * IQR) & (df['A'] <= Q3 + 1.5 * IQR)]

# Cap outliers (winsorization)
df['A_capped'] = df['A'].clip(lower=df['A'].quantile(0.05), 
                              upper=df['A'].quantile(0.95))
```

## Feature Engineering

Feature engineering is the process of creating new features from existing data to improve model performance.

```python
# Create a sample DataFrame
df = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=5),
    'Value_A': [10, 20, 30, 40, 50],
    'Value_B': [5, 10, 15, 20, 25],
    'Category': ['X', 'Y', 'X', 'Y', 'X']
})

# Extract components from datetime
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['DayOfWeek'] = df['Date'].dt.dayofweek

# Mathematical transformations
df['Value_A_squared'] = df['Value_A'] ** 2
df['Value_A_log'] = np.log1p(df['Value_A'])  # log(1+x) to handle zeros

# Interaction features
df['A_times_B'] = df['Value_A'] * df['Value_B']
df['A_plus_B'] = df['Value_A'] + df['Value_B']
df['A_div_B'] = df['Value_A'] / df['Value_B']

# Binning continuous variables
df['Value_A_bins'] = pd.cut(df['Value_A'], bins=3, labels=['Low', 'Medium', 'High'])

# One-hot encoding categorical variables
df_encoded = pd.get_dummies(df, columns=['Category'], prefix=['Cat'])
```

## Normalization and Standardization

```python
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Create sample data
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

# Min-Max Normalization (scales to range [0,1])
scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Z-score Standardization (mean=0, std=1)
scaler = StandardScaler()
df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Manual implementation
df_norm_manual = (df - df.min()) / (df.max() - df.min())
df_std_manual = (df - df.mean()) / df.std()
```

## Data Aggregation and Grouping

```python
# Create sample data
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'SubCategory': ['X', 'X', 'Y', 'Y', 'X', 'Y'],
    'Value': [10, 20, 30, 40, 50, 60]
})

# Group by one column
grouped = df.groupby('Category')
print(grouped['Value'].mean())

# Group by multiple columns
multi_grouped = df.groupby(['Category', 'SubCategory'])
print(multi_grouped['Value'].mean())

# Multiple aggregations
aggs = grouped.agg({
    'Value': ['min', 'max', 'mean', 'sum', 'count']
})

# Custom aggregation function
def range_func(x):
    return x.max() - x.min()

custom_agg = grouped.agg({
    'Value': [range_func, 'std']
})

# Transform groups
df['Value_Normalized'] = grouped['Value'].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

## Reshaping Data

```python
# Create sample data
df = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Category': ['A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40]
})

# Wide format (pivot)
pivot_df = df.pivot(index='Date', columns='Category', values='Value')

# Long format (melt)
df_wide = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02'],
    'A': [10, 30],
    'B': [20, 40]
})
df_long = pd.melt(df_wide, id_vars=['Date'], value_vars=['A', 'B'],
                 var_name='Category', value_name='Value')

# Stack and unstack
stacked = pivot_df.stack().reset_index()
stacked.columns = ['Date', 'Category', 'Value']
unstacked = stacked.set_index(['Date', 'Category']).unstack()
```

## Handling Imbalanced Data

```python
from sklearn.utils import resample

# Create imbalanced dataset
df = pd.DataFrame({
    'Category': ['A'] * 90 + ['B'] * 10,
    'Value': np.random.randn(100)
})

# Upsample minority class
df_minority = df[df['Category'] == 'B']
df_majority = df[df['Category'] == 'A']

df_minority_upsampled = resample(df_minority, 
                                replace=True,     # Sample with replacement
                                n_samples=len(df_majority),    # Match majority class
                                random_state=42)  # Reproducible results

df_balanced = pd.concat([df_majority, df_minority_upsampled])

# Downsample majority class
df_majority_downsampled = resample(df_majority,
                                  replace=False,    # Sample without replacement
                                  n_samples=len(df_minority),  # Match minority class
                                  random_state=42)  # Reproducible results

df_balanced = pd.concat([df_majority_downsampled, df_minority])
```

## Data Validation

```python
# Basic validation checks
def validate_dataframe(df):
    print(f"Shape: {df.shape}")
    print(f"Missing values: {df.isnull().sum().sum()}")
    print(f"Duplicated rows: {df.duplicated().sum()}")
    print("\nData types:")
    print(df.dtypes)
    print("\nSummary statistics:")
    print(df.describe())
    
    # Check for outliers (Z-score method)
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        z_scores = abs(stats.zscore(df[col].dropna()))
        outliers = (z_scores > 3).sum()
        print(f"Outliers in {col}: {outliers}")

# Validate value ranges
def validate_ranges(df, rules):
    """
    rules = {
        'Age': {'min': 0, 'max': 120},
        'Salary': {'min': 0}
    }
    """
    for col, rule in rules.items():
        if 'min' in rule:
            invalid = (df[col] < rule['min']).sum()
            print(f"Values below minimum in {col}: {invalid}")
        if 'max' in rule:
            invalid = (df[col] > rule['max']).sum()
            print(f"Values above maximum in {col}: {invalid}")
```

## Conclusion

Data cleaning and transformation are essential skills for any data analyst or data scientist. Clean, well-structured data is the foundation for accurate analysis and modeling. By mastering these techniques, you'll be able to handle real-world data challenges effectively and prepare your data for advanced analytics and machine learning applications.
