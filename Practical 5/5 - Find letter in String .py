# Python program to find the index of a letter in a word

def find_letter(word, letter):
    for i in range(len(word)):
        if word[i] == letter:
            return i
    return -1

print(find_letter("program", "p"))   # Output: 0
print(find_letter("python", "p"))    # Output: 0
print(find_letter("python", "z"))    # Output: -1
