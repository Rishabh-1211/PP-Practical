from array import array

a = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

slice1 = a[3:8]
print(slice1)

slice2 = a[5:]
print(slice2)

slice3 = a[:5]
print(slice3)

slice4 = a[:]
print(slice4)
