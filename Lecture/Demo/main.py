Dictionary Operations
Cell 19 — Creating a Dictionary
# Creating a dictionary


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


print(student)
Cell 20 — Accessing a Value
# Accessing a value using []


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


print(student["name"])
Cell 21 — Accessing Using get()
# Safer way to access a dictionary value


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


print(student.get("name"))

You can also see the difference when the key doesn't exist:

student = {
    "id": 101,
    "name": "John",
    "age": 20
}


print(student.get("city"))

get() returns None instead of producing a KeyError.

Cell 22 — Adding an Item
# Adding a new item


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


student["city"] = "Mumbai"


print(student)
Cell 23 — Updating an Item
# Updating an existing item


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


student["age"] = 21


print(student)
Cell 24 — Removing Using pop()
# Removing an item using pop()


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


student.pop("age")


print(student)
Cell 25 — Removing Using del
# Removing an item using del


student = {
    "id": 101,
    "name": "John",
    "age": 20,
    "city": "Mumbai"
}


del student["city"]


print(student)
Cell 26 — Clearing a Dictionary
# Removing all items


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


student.clear()


print(student)
Cell 27 — Searching for a Key
# Searching for a key


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


print("name" in student)
print("city" in student)
Cell 28 — Dictionary Keys
# Getting all keys


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


print(student.keys())
Cell 29 — Dictionary Values
# Getting all values


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


print(student.values())
Cell 30 — Dictionary Items
# Getting key-value pairs


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


print(student.items())
Cell 31 — Looping Through Dictionary
# Looping through keys


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


for key in student:
    print(key, student[key])
Cell 32 — Looping Through Keys and Values
# Looping using items()


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


for key, value in student.items():
    print(key, value)
Cell 33 — Copying a Dictionary
# Copying a dictionary


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


copy_dict = student.copy()


print("Original:", student)
print("Copy:", copy_dict)
Cell 34 — Length of a Dictionary
# Finding the length of a dictionary


student = {
    "id": 101,
    "name": "John",
    "age": 20
}


print("Length:", len(student))
Cell 35 — Merging Dictionaries
# Merging two dictionaries


d1 = {
    "a": 1
}


d2 = {
    "b": 2
}


d1.update(d2)


print(d1)
Cell 36 — Dictionary Comprehension
# Dictionary comprehension


squares = {
    x: x * x
    for x in range(1, 6)
}


print(squares)
Part 3 — Extra Practice

Since you're learning these operations, I'd also add a few cells where you can experiment.

Cell 37 — Tuple Practice
# Practice


numbers = (10, 20, 30, 40, 50)


print("First:", numbers[0])
print("Last:", numbers[-1])
print("Slice:", numbers[1:4])
print("Length:", len(numbers))
print("30 exists:", 30 in numbers)
print("Position of 40:", numbers.index(40))
Cell 38 — Dictionary Practice
# Practice


student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python"
}


print("Name:", student["name"])
print("Age:", student["age"])


student["city"] = "Mumbai"


print("After adding city:")
print(student)


student["age"] = 23


print("After updating age:")
print(student)
Cell 39 — Tuple vs Dictionary
# Tuple


numbers = (10, 20, 30)


print("Tuple:", numbers)
print("First element:", numbers[0])




# Dictionary


student = {
    "name": "John",
    "age": 20
}


print("Dictionary:", student)
print("Name:", student["name"])
Important point about your "reference" problem

You're correct to be careful about this.

For example, if you do:

numbers = (1, 2, 3)


numbers = numbers + (4,)
print(numbers)

and then later reuse numbers, you're working with the new value assigned to numbers.

For your learning notebook, the simplest solution is exactly what you've requested:

# Cell A
numbers = (1, 2, 3)
numbers = numbers + (4,)
print(numbers)

Then in the next cell:

# Cell B
numbers = (1, 2, 3)
print(numbers)

Each cell starts with a fresh tuple.

Likewise for dictionaries:

# Cell A
student = {
    "name": "John",
    "age": 20
}


student["age"] = 21


print(student)

Next cell:

# Cell B
student = {
    "name": "John",
    "age": 20
}


student["city"] = "Mumbai"


print(student)