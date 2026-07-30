import numpy as np

# Define two 2D NumPy arrays
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication
product = np.matmul(A, B)
# Alternatively: product = A @ B

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Multiplication (A × B):")
print(product)
