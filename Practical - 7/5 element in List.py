list1 = []

for i in range(5):
    num = int(input(f"Enter integer {i+1}: "))
    list1.append(num)

# Copy elements into another list in reverse order
list2 = list1[::-1]

# Print both lists
print("Original list:", list1)
print("Reversed list:", list2)

# Using reverse() function
list1.reverse()
print(list1)
