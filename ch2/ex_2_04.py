"""
Problem: You want to match or search text for a specific pattern
"""

import re

text = "Yeah, but no, but yeah, but really no, but yeah."

print("text: {}".format(text))
print("text == 'yeah'", text == "yeah")
print("text.startswith('Yeah')", text.startswith('Yeah'))
print("text.endswith('no')", text.endswith('no'))

print("text.find('no')", text.find('no'))

datepat = re.compile(r'\d+/\d+/\d+')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

# We can flag "capture groups" by enclosing parts of an re in parentheses

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group())

