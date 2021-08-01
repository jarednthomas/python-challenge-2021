#!/usr/bin/env python3
import string

key = 2
# Define charset as ascii_lowercase and shift by key
alphabet = string.ascii_lowercase
shifted = alphabet[key:] + alphabet[:key]

# Apply translation table to given hint
hint = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
decoder = hint.maketrans(alphabet, shifted)
#print(hint.translate(decoder))

# Per hint, apply decoder to the end of the url
url = "http://www.pythonchallenge.com/pc/def/map.html"
print(url.replace("map", "map".translate(decoder)))
