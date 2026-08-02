list = ['physics', 'chemistry', 1997, 2000]

# append() - adds an element at the end of the list
list.append('maths')
print("After append():", list)


# insert() - adds an element at a specific index
list.insert(2, 'biology')
print("After insert():", list)

# extend() - Add all elements of a list to the another list 
list.extend([9, 11, 13]) 
print("After extend():", list)