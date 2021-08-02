#!/usr/bin/env python3
# Hint: inflate (busy bee) -> bz2 compression

import bz2, requests
from bs4 import BeautifulSoup, Comment

# Parse comments
url = "http://www.pythonchallenge.com/pc/def/integrity.html"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Extract comments from soup and save last
comments = soup.find_all(text=lambda text: isinstance(text, Comment))
last_comment = comments[-1]
print(last_comment)

# Return username and password for next level
print("Username:", bz2.decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084").decode())
print("Password:", bz2.decompress(b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08").decode())
