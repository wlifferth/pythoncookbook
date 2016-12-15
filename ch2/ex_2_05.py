"""
Problem: You want to search for an replace a text pattern in a string.
"""

text = "yeah, but no, but yeah, but really no, but yeah"

print(text.replace("yeah", "yep"))

import re

a = "Today is 11/27/2012/. PyCon starts 3/13/2013"
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(a))
