# Python program to count the number of times 'a' appears in a word

word = "python programming"
count = 0

for letter in word:
    if letter == 'a':
        count += 1

print(count)
