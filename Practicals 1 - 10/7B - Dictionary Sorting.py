# Practical 7B - Dictionary Sorting

# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}
# student = {'name': 'Rahul', 'age': 20, 'marks': 85}

# Accessing values
print(student["name"])
# Access value using key
# Output: Rahul

print(student.get("age"))
# Access value using get()
# Output: 20
# get() returns None if key doesn't exist instead of raising an error

# Adding a new key-value pair
student["city"] = "Mumbai"
# Adds a new key-value pair
# student = {'name': 'Rahul', 'age': 20, 'marks': 85, 'city': 'Mumbai'}

# Updating a value
student["marks"] = 90
# Updates existing value for key 'marks'
# student = {'name': 'Rahul', 'age': 20, 'marks': 90, 'city': 'Mumbai'}

# Removing elements
student.pop("age")
# Removes key 'age' and returns its value
# student = {'name': 'Rahul', 'marks': 90, 'city': 'Mumbai'}

# del student["city"]
# Another way to remove a key-value pair

# student.clear()
# Removes all key-value pairs from the dictionary

# Getting keys, values, and items
print(student.keys())
# Returns all keys
# Output: dict_keys(['name', 'marks', 'city'])

print(student.values())
# Returns all values
# Output: dict_values(['Rahul', 90, 'Mumbai'])

print(student.items())
# Returns key-value pairs as tuples
# Output: dict_items([('name', 'Rahul'), ('marks', 90), ('city', 'Mumbai')])

# Checking if a key exists
print("name" in student)
# Checks whether key 'name' exists
# Output: True

# Length of dictionary
print(len(student))
# Returns total number of key-value pairs
# Output: 3

# Copying dictionary
new_student = student.copy()
# Creates a separate copy of the dictionary
# new_student = {'name': 'Rahul', 'marks': 90, 'city': 'Mumbai'}

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)
# Iterates through each key-value pair
# Output:
# name : Rahul
# marks : 90
# city : Mumbai