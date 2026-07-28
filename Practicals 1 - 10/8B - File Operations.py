# Practical 8B - File Operations.py

import os

# Create and Write to a File
with open("sample.txt", "w") as file:
    file.write("Hello World\n")
    file.write("Welcome to Python\n")
# Creates a file named sample.txt in write mode.
# If the file already exists, its contents are overwritten.
# Writes two lines into the file.

print("Data written successfully.\n")

# Read Entire File
with open("sample.txt", "r") as file:
    print("Reading Entire File:")
    print(file.read())
# Opens the file in read mode.
# read() reads the entire contents of the file at once.

# Append Data
with open("sample.txt", "a") as file:
    file.write("This line is appended.\n")
# Opens the file in append mode.
# New data is added at the end without removing existing content.

print("\nData appended successfully.")

# Read Line by Line
with open("sample.txt", "r") as file:
    print("\nReading Line by Line:")
    for line in file:
        print(line.strip())
# Reads one line at a time using a loop.
# strip() removes extra newline characters.

# Readlines()
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("\nUsing readlines():")
    print(lines)
# readlines() returns all lines as a list.
# Each line is stored as a separate element.

# tell() - Current File Position
with open("sample.txt", "r") as file:
    print("\nInitial Position:", file.tell())
    # tell() returns the current cursor position.
    # Output: 0

    file.read(5)
    # Reads first 5 characters: "Hello"

    print("Position after reading 5 chars:", file.tell())
    # Cursor moves to position 5.
    # Output: 5

# seek() - Move File Pointer
with open("sample.txt", "r") as file:
    file.seek(6)
    # Moves cursor to position 6.

    print("\nAfter seek(6):")
    print(file.read())
# Reads data starting from character position 6.

# Check if File Exists
if os.path.exists("sample.txt"):
    print("\nFile exists.")
# Checks whether sample.txt is present in the current directory.

# Rename File
os.rename("sample.txt", "data.txt")
# Renames sample.txt to data.txt.

print("File renamed to data.txt")

# Delete File
os.remove("data.txt")
# Permanently deletes data.txt.

print("File deleted successfully.")