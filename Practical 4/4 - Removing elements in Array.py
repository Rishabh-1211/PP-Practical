from array import array

a = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a)

# Remove first occurrence of 1
a.remove(1)
print(a)

# Remove element at index 2
a.pop(2)
print(a)
