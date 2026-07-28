# Practical 8A - Function with Tuples

# Creating a tuple
numbers = (10, 20, 30, 40)
# numbers = (10, 20, 30, 40)

# Accessing elements
print(numbers[0])
# Access first element using index 0
# Output: 10

print(numbers[-1])
# Access last element using negative indexing
# Output: 40

# Slicing
print(numbers[1:3])
# Returns elements from index 1 up to (but not including) index 3
# Output: (20, 30)

# Searching
print(20 in numbers)
# Checks whether 20 exists in the tuple
# Output: True

print(numbers.index(30))
# Returns index position of value 30
# Output: 2

# Counting occurrences
data = (10, 20, 10, 30, 10)
# data = (10, 20, 10, 30, 10)

print(data.count(10))
# Counts how many times 10 appears
# Output: 3

# Length
print(len(numbers))
# Returns total number of elements
# Output: 4

# Maximum, Minimum, Sum
print(max(numbers))
# Returns largest value
# Output: 40

print(min(numbers))
# Returns smallest value
# Output: 10

print(sum(numbers))
# Returns sum of all elements
# Output: 100

# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)

print(tuple1 + tuple2)
# Combines two tuples into one
# Output: (1, 2, 3, 4)

# Repetition
print(tuple1 * 3)
# Repeats the tuple three times
# Output: (1, 2, 1, 2, 1, 2)

# Tuple unpacking
a, b, c = (100, 200, 300)

print(a, b, c)
# Assigns tuple values to separate variables
# a = 100, b = 200, c = 300
# Output: 100 200 300

# Nested tuple
nested = ((1, 2), (3, 4))
# nested = ((1, 2), (3, 4))

print(nested[1][0])
# Access second tuple (index 1) and first element (index 0)
# Output: 3

# Converting tuple to list
temp = list(numbers)
# Converts tuple into a list
# temp = [10, 20, 30, 40]

temp.append(50)
# Adds 50 to the list
# temp = [10, 20, 30, 40, 50]

# Converting back to tuple
numbers = tuple(temp)
# Converts list back into a tuple
# numbers = (10, 20, 30, 40, 50)

print(numbers)
# Output: (10, 20, 30, 40, 50)