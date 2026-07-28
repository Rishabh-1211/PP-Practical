import numpy as np

# Create NumPy array
arr = np.array([1, 2, 3])

# Access first element
print("First element:", arr[0])

# Add element
arr = np.append(arr, 5)

print("Updated array:", arr)

# Display all elements
print("Array elements:")
for i in arr:
    print(i, end=" ")
