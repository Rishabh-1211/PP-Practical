# Practical 9A - Regular Expressions

import re

text = "Contact us at support123@gmail.com or call 9876543210"
# Sample text containing an email address and a phone number.

# Extract email
email = re.findall(r'\S+@\S+', text)
# re.findall() searches the text for all matches of the pattern.
# \S+ matches one or more non-whitespace characters.
# @ matches the '@' symbol.
# This pattern extracts email-like strings.
# Output: ['support123@gmail.com']

# Extract numbers
numbers = re.findall(r'\d+', text)
# \d+ matches one or more digits.
# Extracts all numeric values from the text.
# Output: ['123', '9876543210']
# Note: '123' is extracted because it appears in the email address.

print("Email:", email)
# Output: Email: ['support123@gmail.com']

print("Numbers:", numbers)
# Output: Numbers: ['123', '9876543210']