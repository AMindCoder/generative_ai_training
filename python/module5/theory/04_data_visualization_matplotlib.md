# Basic Data Visualization with Matplotlib

Data visualization is a crucial part of data analysis. It helps us understand patterns, trends, and relationships in data that might not be apparent from looking at raw numbers. Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

## Introduction to Matplotlib

Matplotlib is organized into a hierarchy of objects:

- **Figure**: The top-level container for all plot elements
- **Axes**: The actual plot area where data is plotted
- **Axis**: The number-line-like objects that define the boundaries of the plot
- **Artist**: Everything visible on the figure (lines, text, legends, etc.)

Matplotlib provides two main interfaces:

1. **Pyplot API**: A MATLAB-like interface that automatically creates and manages figures and axes
2. **Object-Oriented API**: More flexible and powerful, giving explicit control over figure and axes objects

## Setting Up

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set style
plt.style.use('seaborn-v0_8-whitegrid')  # Modern style

# For Jupyter notebooks, use:
%matplotlib inline
```

## Basic Line Plot

```python
# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data
ax.plot(x, y, label='sin(x)')

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Simple Line Plot')

# Add grid and legend
ax.grid(True)
ax.legend()

# Show plot
plt.tight_layout()
plt.show()
```

## Multiple Lines

```python
# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot multiple lines
ax.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2)
ax.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Multiple Line Plot')

# Add grid and legend
ax.grid(True)
ax.legend()

# Show plot
plt.tight_layout()
plt.show()
```

## Scatter Plot

```python
# Generate random data
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create scatter plot
scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')

# Add a colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Color Value')

# Add labels and title
ax.set_xlabel('X Value')
ax.set_ylabel('Y Value')
ax.set_title('Scatter Plot')

# Show plot
plt.tight_layout()
plt.show()
```

## Bar Chart

```python
# Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 55, 15]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create bar chart
bars = ax.bar(categories, values, color='skyblue', edgecolor='black', alpha=0.7)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{height}', ha='center', va='bottom')

# Add labels and title
ax.set_xlabel('Category')
ax.set_ylabel('Value')
ax.set_title('Bar Chart')

# Customize ticks
ax.set_ylim(0, max(values) * 1.2)

# Show plot
plt.tight_layout()
plt.show()
```

## Horizontal Bar Chart

```python
# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [25, 40, 30, 55, 15]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create horizontal bar chart
bars = ax.barh(categories, values, color='lightgreen', edgecolor='black', alpha=0.7)

# Add value labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2., 
            f'{width}', ha='left', va='center')

# Add labels and title
ax.set_xlabel('Value')
ax.set_ylabel('Category')
ax.set_title('Horizontal Bar Chart')

# Show plot
plt.tight_layout()
plt.show()
```

## Histogram

```python
# Generate random data
np.random.seed(42)
data = np.random.normal(0, 1, 1000)  # 1000 points from normal distribution

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create histogram
n, bins, patches = ax.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Add a line showing the expected distribution
x = np.linspace(-4, 4, 100)
y = 1/(1 * np.sqrt(2 * np.pi)) * np.exp( - (x - 0)**2 / (2 * 1**2)) * len(data) * (bins[1] - bins[0])
ax.plot(x, y, 'r--', linewidth=2)

# Add labels and title
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.set_title('Histogram')

# Show plot
plt.tight_layout()
plt.show()
```

## Pie Chart

```python
# Data
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 25, 10, 20]
explode = (0, 0.1, 0, 0, 0)  # explode the 2nd slice

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create pie chart
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, colors=plt.cm.Paired.colors)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Add title
ax.set_title('Pie Chart')

# Show plot
plt.tight_layout()
plt.show()
```

## Box Plot

```python
# Generate random data
np.random.seed(42)
data = [np.random.normal(0, std, 100) for std in range(1, 6)]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create box plot
ax.boxplot(data, patch_artist=True, 
           boxprops=dict(facecolor='lightblue', color='black'),
           whiskerprops=dict(color='black'),
           capprops=dict(color='black'),
           medianprops=dict(color='red'))

# Add labels and title
ax.set_xlabel('Group')
ax.set_ylabel('Value')
ax.set_title('Box Plot')

# Set x-tick labels
ax.set_xticklabels(['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'])

# Show plot
plt.tight_layout()
plt.show()
```

## Heatmap

```python
# Generate random data
np.random.seed(42)
data = np.random.rand(10, 10)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Create heatmap
im = ax.imshow(data, cmap='viridis')

# Add colorbar
cbar = fig.colorbar(im, ax=ax)
cbar.set_label('Value')

# Add labels and title
ax.set_title('Heatmap')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Add tick marks
ax.set_xticks(np.arange(data.shape[1]))
ax.set_yticks(np.arange(data.shape[0]))

# Add tick labels
ax.set_xticklabels([f'X{i}' for i in range(data.shape[1])])
ax.set_yticklabels([f'Y{i}' for i in range(data.shape[0])])

# Rotate the tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        text = ax.text(j, i, f'{data[i, j]:.2f}',
                       ha="center", va="center", color="white" if data[i, j] > 0.5 else "black")

# Show plot
plt.tight_layout()
plt.show()
```

## Subplots

```python
# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x/10)

# Create figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot on each subplot
axs[0, 0].plot(x, y1, 'b-')
axs[0, 0].set_title('Sine')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('sin(x)')

axs[0, 1].plot(x, y2, 'r-')
axs[0, 1].set_title('Cosine')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('cos(x)')

axs[1, 0].plot(x, y3, 'g-')
axs[1, 0].set_title('Tangent')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('tan(x)')
axs[1, 0].set_ylim(-5, 5)  # Limit y-axis for better visibility

axs[1, 1].plot(x, y4, 'm-')
axs[1, 1].set_title('Exponential Decay')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('exp(-x/10)')

# Adjust layout
plt.tight_layout()
plt.show()
```

## Time Series Plot

```python
# Generate time series data
dates = pd.date_range('2023-01-01', periods=100)
values = np.cumsum(np.random.randn(100))  # Random walk

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot time series
ax.plot(dates, values, 'b-')

# Format x-axis with dates
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# Add labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.set_title('Time Series Plot')

# Add grid
ax.grid(True)

# Show plot
plt.tight_layout()
plt.show()
```

## 3D Plot

```python
from mpl_toolkits.mplot3d import Axes3D

# Generate data for 3D plot
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create surface plot
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)

# Add colorbar
cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
cbar.set_label('Z Value')

# Add labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot')

# Show plot
plt.tight_layout()
plt.show()
```

## Customizing Plots

### Colors and Styles

```python
# Available styles
print(plt.style.available)

# Set style
plt.style.use('seaborn-v0_8-darkgrid')

# Color maps
print(plt.colormaps())

# Custom colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
```

### Text and Annotations

```python
# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)

# Add text
ax.text(4, 0.8, 'Local Maximum', fontsize=12, ha='center')

# Add annotation with arrow
ax.annotate('Local Minimum', xy=(7.85, -1), xytext=(9, -0.5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

# Add a title with custom font
ax.set_title('Sine Wave with Annotations', fontsize=16, fontweight='bold')

# Add a text box
textstr = 'Important Note:\nThis is a sine wave\nwith period 2π'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

# Show plot
plt.tight_layout()
plt.show()
```

### Legends and Colorbars

```python
# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot multiple lines
x = np.linspace(0, 10, 100)
line1, = ax.plot(x, np.sin(x), label='Sine')
line2, = ax.plot(x, np.cos(x), label='Cosine')
line3, = ax.plot(x, np.sin(x) * np.cos(x), label='Sine * Cosine')

# Add legend with custom properties
legend = ax.legend(loc='upper right', shadow=True, fontsize='large')

# Add a frame to the legend
frame = legend.get_frame()
frame.set_facecolor('lightgray')
frame.set_edgecolor('black')

# Show plot
plt.tight_layout()
plt.show()
```

### Saving Figures

```python
# Create a plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(np.random.randn(1000).cumsum())
ax.set_title('Random Walk')

# Save figure in different formats
fig.savefig('plot.png', dpi=300, bbox_inches='tight')  # PNG format
fig.savefig('plot.pdf', bbox_inches='tight')  # PDF format
fig.savefig('plot.svg', bbox_inches='tight')  # SVG format
```

## Integration with Pandas

Pandas has built-in plotting functionality that uses Matplotlib under the hood:

```python
# Create a DataFrame
df = pd.DataFrame({
    'A': np.random.randn(1000).cumsum(),
    'B': np.random.randn(1000).cumsum(),
    'C': np.random.randn(1000).cumsum(),
    'D': np.random.randn(1000).cumsum()
})

# Line plot
df.plot(figsize=(10, 6), title='Line Plot')

# Bar plot
df.iloc[0:10].plot.bar(figsize=(10, 6), title='Bar Plot')

# Histogram
df.plot.hist(bins=20, alpha=0.5, figsize=(10, 6), title='Histogram')

# Scatter plot
df.plot.scatter(x='A', y='B', figsize=(10, 6), title='Scatter Plot')

# Box plot
df.plot.box(figsize=(10, 6), title='Box Plot')

# Area plot
df.plot.area(alpha=0.5, figsize=(10, 6), title='Area Plot')

# Pie chart
df.iloc[0].plot.pie(figsize=(10, 6), title='Pie Chart')
```

## Conclusion

Matplotlib is a powerful and flexible library for creating a wide variety of visualizations in Python. This introduction covers the basics, but there's much more to explore. As you become more comfortable with Matplotlib, you can create more complex and customized visualizations to effectively communicate your data insights.

For more advanced visualizations, consider exploring other libraries built on top of Matplotlib, such as Seaborn (for statistical visualizations) and Plotly (for interactive visualizations).
