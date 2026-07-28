# Practical 6A - String Processing

text = "Python Programming"

# Accessing string elements
print("First character:", text[0])
print("Second character:", text[1])
print("Last character:", text[-1])

# Accessing a range of characters (slicing)
print("First 6 characters:", text[0:6])
print("Programming word:", text[7:])
print("Characters 2 to 5:", text[2:6])

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Count characters
print("Length:", len(text))

# Replace a word
new_text = text.replace("Programming", "Language")
print("Modified String:", new_text)

# Split string into words
words = text.split()
print("Words:", words)