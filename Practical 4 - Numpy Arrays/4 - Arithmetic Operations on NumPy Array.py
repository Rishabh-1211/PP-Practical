import numpy as np

a = np.array([1,3,5,7])
b = np.array([2,4,6,8])

result = a + b
print(result)

result = a - b
print(result)

result = a * b
print(result)

result = a / b
print(result)


print("Addition:", np.add(a,b))
print("Subtraction:", np.subtract(a,b))
print("Multiplication:", np.multiply(a,b))
print("Division:", np.divide(a,b))
