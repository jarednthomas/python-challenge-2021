#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup, Comment

# Set url and headers
url = "http://www.pythonchallenge.com/pc/def/ocr.html"
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

counts = {}
# Iterate through last comment, counting instances of each char
for char in last_comment:
    if char not in counts:
        counts[char] = 1
    else:
        counts[char] += 1

solution = []
# Iterate through counts, storing values of 1
for key in counts:
    if counts[key] == 1:
        solution.append(key)

# Return answer url
answer = "".join(solution)
print(url.replace("ocr", answer))