# Practical 9C - Regular Expression & HTML Processing

# pip install beautifulsoup4

import re
from bs4 import BeautifulSoup

html = """
<html>
<body>
<p>Contact: admin@gmail.com</p>
<p>Phone: 9876543210</p>
</body>
</html>
"""
# Sample HTML content containing an email address and a phone number.

# HTML Parsing
soup = BeautifulSoup(html, "html.parser")
# Parses the HTML document and creates a BeautifulSoup object.

# Extract plain text from HTML
text = soup.get_text()
# get_text() removes HTML tags and returns only the text content.
# Result:
# "\nContact: admin@gmail.com\nPhone: 9876543210\n"

# Regex Extraction

emails = re.findall(r'\S+@\S+', text)
# Finds email-like patterns.
# \S+ matches one or more non-whitespace characters.
# @ matches the '@' symbol.
# Output: ['admin@gmail.com']

phones = re.findall(r'\d+', text)
# Finds sequences of digits.
# \d+ matches one or more digits.
# Output: ['9876543210']

print("Emails:", emails)
# Output: Emails: ['admin@gmail.com']

print("Phones:", phones)
# Output: Phones: ['9876543210']