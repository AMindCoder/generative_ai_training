**Module 1: Introduction to Python**  
**Chapter 4: Control Structures**  

---

### **1. Conditional Statements**
Control structures help us make decisions and control the flow of our ML programs. Let's explore them with practical machine learning examples.

#### **if-elif-else Statements**
```python
# Basic model evaluation
accuracy = 0.95

if accuracy >= 0.95:
    print("Model performance is excellent!")
elif accuracy >= 0.85:
    print("Model performance is good")
else:
    print("Model needs improvement")

# Checking model requirements
batch_size = 32
gpu_memory = 8  # GB

if gpu_memory >= 16:
    batch_size = 64
    print("Using large batch size")
elif gpu_memory >= 8:
    batch_size = 32
    print("Using medium batch size")
else:
    batch_size = 16
    print("Using small batch size")
```

### **2. Loops**

#### **for Loops**
```python
# Iterating through epochs
num_epochs = 5
for epoch in range(num_epochs):
    print(f"Training epoch {epoch + 1}/{num_epochs}")

# Processing a batch of data
batch = [1, 2, 3, 4, 5]
for data_point in batch:
    processed_data = data_point * 2
    print(f"Processed: {processed_data}")

# Iterating through dataset with enumeration
dataset = ['image1.jpg', 'image2.jpg', 'image3.jpg']
for i, filename in enumerate(dataset):
    print(f"Processing image {i+1}: {filename}")
```

#### **while Loops**
```python
# Training loop with convergence criterion
current_loss = 1.0
epoch = 0
target_loss = 0.1

while current_loss > target_loss:
    # Simulated training iteration
    current_loss *= 0.8
    epoch += 1
    print(f"Epoch {epoch}: Loss = {current_loss:.4f}")

# Early stopping implementation
patience = 3
no_improvement = 0
best_loss = float('inf')

while no_improvement < patience:
    new_loss = get_validation_loss()  # Placeholder function
    if new_loss < best_loss:
        best_loss = new_loss
        no_improvement = 0
    else:
        no_improvement += 1
```

### **3. Loop Control Statements**

#### **break and continue**
```python
# Early stopping with break
for epoch in range(100):
    loss = compute_loss()  # Placeholder function
    if loss < 0.001:
        print("Reached target loss. Stopping training.")
        break

# Skip processing for invalid data using continue
for data in dataset:
    if data is None:
        continue
    process_data(data)  # Placeholder function
```

### **4. Basic Input/Output**

#### **print() Function**
```python
# Basic printing
print("Starting model training...")

# Formatted printing for ML metrics
accuracy = 0.956
loss = 0.123
print(f"Model Performance: Accuracy = {accuracy:.2%}, Loss = {loss:.4f}")

# Printing multiple metrics
metrics = {
    'accuracy': 0.95,
    'precision': 0.92,
    'recall': 0.89
}
for metric, value in metrics.items():
    print(f"{metric.capitalize()}: {value:.2%}")
```

#### **input() Function**
```python
# Getting user input for model parameters
learning_rate = float(input("Enter learning rate (default 0.001): ") or 0.001)
num_epochs = int(input("Enter number of epochs: "))

# Confirming model training
confirm = input("Start model training? (yes/no): ")
if confirm.lower() == 'yes':
    print("Training started...")
else:
    print("Training cancelled")
```

### **5. Best Practices**

1. **Loop Efficiency**
   ```python
   # Prefer this
   for i in range(len(dataset)):
       # Process directly with index
   
   # Over this
   i = 0
   while i < len(dataset):
       # Process with counter
       i += 1
   ```

2. **Conditional Statement Design**
   ```python
   # Good Practice
   if condition1:
       action1()
   elif condition2:
       action2()
   else:
       default_action()
   
   # Avoid nested if statements when possible
   if condition1:
       if condition2:
           if condition3:
               action()  # Too many levels of nesting
   ```

### **Practice Exercises**
1. Create a training loop with early stopping
2. Implement a data preprocessing pipeline using loops
3. Build a simple model evaluation system using conditionals
4. Create an interactive model configuration setup using input()

### **Key Takeaways**
- Control structures are essential for managing ML workflow
- Loops help in iterating through datasets and training epochs
- Conditional statements enable dynamic model behavior
- Proper I/O handling is crucial for model monitoring and user interaction
- Clean code practices improve maintainability and readability
