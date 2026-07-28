# Practical 7A - List Operations

# Creating a list
numbers = [10, 20, 30, 40]
# numbers = [10, 20, 30, 40]

# Accessing elements
print(numbers[0])      # Access first element (index starts from 0) → 10
print(numbers[-1])     # Access last element using negative indexing → 40

# Adding elements
numbers.append(50)
# Adds 50 at the end
# numbers = [10, 20, 30, 40, 50]

numbers.insert(2, 25)
# Inserts 25 at index 2
# numbers = [10, 20, 25, 30, 40, 50]

# Extending a list
numbers.extend([60, 70])
# Adds multiple elements to the end
# numbers = [10, 20, 25, 30, 40, 50, 60, 70]

# Removing elements
numbers.remove(25)
# Removes the first occurrence of value 25
# numbers = [10, 20, 30, 40, 50, 60, 70]

numbers.pop()
# Removes and returns the last element (70)
# numbers = [10, 20, 30, 40, 50, 60]

numbers.pop(1)
# Removes and returns element at index 1 (20)
# numbers = [10, 30, 40, 50, 60]

# Updating elements
numbers[0] = 100
# Replaces element at index 0 with 100
# numbers = [100, 30, 40, 50, 60]

# Slicing
print(numbers[1:4])
# Returns elements from index 1 up to (but not including) index 4
# Output: [30, 40, 50]

# Searching
print(30 in numbers)
# Checks whether 30 exists in the list
# Output: True

print(numbers.index(30))
# Returns the index position of 30
# Output: 1

# Counting occurrences
numbers.append(30)
# numbers = [100, 30, 40, 50, 60, 30]

print(numbers.count(30))
# Counts how many times 30 appears
# Output: 2

# Sorting
numbers.sort()
# Sorts list in ascending order
# numbers = [30, 30, 40, 50, 60, 100]

numbers.sort(reverse=True)
# Sorts list in descending order
# numbers = [100, 60, 50, 40, 30, 30]

# Reversing
numbers.reverse()
# Reverses current order of elements
# numbers = [30, 30, 40, 50, 60, 100]

# Copying
new_list = numbers.copy()
# Creates a separate copy of the list
# new_list = [30, 30, 40, 50, 60, 100]

# Length
print(len(numbers))
# Returns total number of elements
# Output: 6

# Maximum, Minimum, Sum
print(max(numbers))
# Largest value → 100

print(min(numbers))
# Smallest value → 30

print(sum(numbers))
# Sum of all elements → 310

# Concatenation
list1 = [1, 2]
list2 = [3, 4]

print(list1 + list2)
# Combines two lists
# Output: [1, 2, 3, 4]

# Repetition
print(list1 * 3)
# Repeats list1 three times
# Output: [1, 2, 1, 2, 1, 2]

# Clearing list
numbers.clear()
# Removes all elements
# numbers = []

print(numbers)
# Output: []