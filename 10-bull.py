#!/usr/bin/env python3

url = "http://www.pythonchallenge.com/pc/return/bull.html"
# Hint: What are you looking at? len(a[30]) = ?

''' Clicking on the bull reveals a sequence
a = [1, 11, 21, 1211, 111221, 
https://www.geeksforgeeks.org/look-and-say-sequence/
'''

def lookSay(n):

    # Catch first two cases
    if (n == 1):
        return "1"
    if (n == 2):
        return "11"

    # Find terms from 3 to (n-1)
    # Initialize counter s at last result
    s = "11"
    for i in range(3, n + 1):

        # prev value is checked at current, dummy variable
        s += '$'
        l = len(s)

        # Initialize counter variables
        cnt = 1
        tmp = ""

        # Iterates over each j in string
        for j in range(1, l):

            # If not matching
            if (s[j] != s[j - 1]):

                # Count
                tmp += str(cnt + 0) 
                # Add to string
                tmp += s[j - 1]
                # Reset count
                cnt = 1

            # Matches, inc count
            else:
                cnt += 1

        s = tmp
    return s

N = 31
#print(lookSay(N))
#print(len(lookSay(N)))
print(url.replace("bull", str(len(lookSay(N)))))