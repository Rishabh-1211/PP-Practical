# Practical 9B - HTML Processing

# pip install beautifulsoup4

from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>Python Tutorial</title>
</head>
<body>
<h1>Welcome to Python</h1>
<p>Learning HTML Processing.</p>
<a href="https://example.com">Visit</a>
</body>
</html>
"""
# Sample HTML document stored as a multi-line string.

# Create BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")
# Parses the HTML content using Python's built-in HTML parser.
# Creates a BeautifulSoup object that allows easy navigation and extraction of data.

# Extract title
print("Title:", soup.title.text)
# soup.title finds the <title> tag.
# .text extracts the text inside the tag.
# Output: Python Tutorial

# Extract heading
print("Heading:", soup.h1.text)
# soup.h1 finds the first <h1> tag.
# .text returns the text content.
# Output: Welcome to Python

# Extract paragraph
print("Paragraph:", soup.p.text)
# soup.p finds the first <p> tag.
# .text extracts the paragraph text.
# Output: Learning HTML Processing.

# Extract hyperlink
print("Link:", soup.a["href"])
# soup.a finds the first <a> tag.
# ["href"] retrieves the value of the href attribute.
# Output: https://example.com