# Lambda function to check if a string starts with 'P'

check_start = lambda word: word.startswith('P')

myword = input("Enter a word: ")

print(check_start("Python"))  # True
print(check_start("Java"))    # False

print(check_start(myword))
