# Practical 4 - Array Indexing - Slicing - Attributes

import numpy as np

# Create a 3x4 NumPy array
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Original Array:")
print(arr)

# Indexing
print("\nIndexing")

# Access element in first row and third column
print("Element at row 1, column 3:", arr[0, 2])

# Access the last element of the array
print("Last element:", arr[-1, -1])

# Slicing
print("\nSlicing")

# Display the first two rows
print("First two rows:")
print(arr[:2, :])

# Display columns 2 and 3
print("\nColumns 2 and 3:")
print(arr[:, 1:3])

# Display a subarray from rows 2-3 and columns 2-4
print("\nSubarray (rows 2-3, columns 2-4):")
print(arr[1:3, 1:4])

# Display alternate columns
print("\nAlternate columns:")
print(arr[:, ::2])

# Array Attributes
print("\nArray Attributes")

# Shape gives rows and columns
print("Shape:", arr.shape)

# Number of dimensions
print("Dimensions:", arr.ndim)

# Total number of elements
print("Total Elements:", arr.size)

# Data type of array elements
print("Data Type:", arr.dtype)

# Memory used by one element
print("Item Size (bytes):", arr.itemsize)

# Total memory used by the array
print("Total Memory Used (bytes):", arr.nbytes)