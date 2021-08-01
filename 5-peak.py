#!/usr/bin/env python3

import pickle
from urllib.request import urlopen

# Load banner.p with pickle library
uri = "http://www.pythonchallenge.com/pc/def/banner.p"
data = pickle.load(urlopen(uri))

# Print data such that i is printed j times
for line in data:
    print("".join([i * j for i, j in line]))

# Return solution url
print(uri.replace("banner.p", "channel.html"))