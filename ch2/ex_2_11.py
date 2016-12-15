"""
Problem: You want to strip unwanted characters, such as whitespace, from the beginning, end, or middle of a text string
"""

s = '       \thello\t  \t\nworld\n   \t'
print(s)
print(s.strip())

t = '-----hello=-=-=-=-='
print(t)
print(t.lstrip('-'))
print(t.strip('-='))

import re
print(re.sub('\s+', ' ', s).strip())

filename = "example.txt"

with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line + "!")
