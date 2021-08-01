#!/usr/bin/env python3
# Hint: linkedlist.php

import re
from urllib.request import urlopen

# n = "12345" # Starting value for nothing
# n = "63579" # Break in chain
n= "66831"    # Final nothing
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
regex = r"[0-9]{3,}"
nothing = re.compile(regex)

# Iterate through each php link
while True:
    content = urlopen(url % n).read().decode('utf-8')
    match = nothing.search(content)

    # Once regex is no longer found you've reached the end
    if match == None:
        answer = content
        break

    # Otherwise set n to nothing found via regex and repeat
    n = match.group(0)

# Return solution url
print(url.replace("linkedlist.php?nothing=%s", answer))
