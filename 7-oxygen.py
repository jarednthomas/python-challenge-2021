#!/usr/bin/env python3
import urllib.request
from PIL import Image

url = "http://www.pythonchallenge.com/pc/def/oxygen.html"

# Open image resource and save locally
resource = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")
output = open("7.png","wb")
output.write(resource.read())
output.close()

# Open image as im 
with Image.open("7.png") as im:

    pix = im.load()
    # Get dimensions of image and set y to midpoint
    w, h = im.size

    ''' Solution
    # Join the red pixel values as chars within the middle of the image (minus 3ish blocks)
    print("".join( [chr(im.getpixel((i, h//2))[0]) for i in range(0, (w-21), 7)] ) )

    # Above hint gives another list, which can be mapped as chars to say "integrity"
    print("".join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121])))
    '''

    # Return solution url
    print(url.replace("oxygen", "integrity"))
    