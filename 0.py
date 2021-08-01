#!/usr/bin/env python3
# Replace 0 in the url with 2^38
print("http://www.pythonchallenge.com/pc/def/0.html".replace("0", str(pow(2, 38))))