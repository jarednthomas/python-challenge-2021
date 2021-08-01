#!/usr/bin/env python3
# Hint: One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

import re, requests
from bs4 import BeautifulSoup, Comment

# Set url and headers
url = "http://www.pythonchallenge.com/pc/def/equality.html"
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

# Parse html with bs4
response = requests.get(url, headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract comments from soup and save last
comments = soup.find_all(text=lambda text: isinstance(text, Comment))
last_comment = comments[-1]

# Find all matches of hint using a regular expression
regex = r"[a-z][A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]"
matches = re.findall(regex, last_comment)

# Return solution url
print(url.replace("equality", "".join( i[4] for i in matches )))