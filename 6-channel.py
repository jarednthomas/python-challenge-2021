#!/usr/bin/env python3
# Hint: now there are pairs (zip)

import io, re, requests, zipfile

def get_comment(fname):
    """ Given a filename
    get comments and return """
    c = zf.getinfo(fname).comment
    return c

# Extract zip contents to current directory
url = "http://www.pythonchallenge.com/pc/def/channel.zip"
response = requests.get(url)
zf = zipfile.ZipFile(io.BytesIO(response.content))
#content = zf.extractall()

# Initial Nothing
n = 90052

# All files are 2 ints or more, set as regex for nothing
regex = r"[0-9]{2,}"  
nothing = re.compile(regex)

# Iterate through all files looking for nothings and save comments
comments = []
while True:

    fname = str(n) + ".txt"
    with open(fname) as f:

        # Read in line to content
        content = f.readline()
        #print(content)

        # Check if line contains nothing, else break
        match = nothing.search(content)
        if match == None:
            break

        # Match found, save comments and set found as next nothing
        else:
            comments.append(get_comment(fname).decode('utf=8'))
            n = match.group(0)

# Print all comments found in order of nothings
print("".join(comments))

# hockey.html: it's in the air. look at the letters -> oxygen
print(url.replace("channel.zip", "oxygen.html"))