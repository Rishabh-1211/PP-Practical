inputString = input("Enter a string: ")

letters = 0
digits = 0

for character in inputString:
    if character.isdigit():
        digits += 1
    elif character.isalpha():
        letters += 1

print("Letters:", letters)
print("Digits:", digits)
