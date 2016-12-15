"""
Problem: You need to split a string into fields, but the delimiters (and spacing around them) aren't consistent throughout the string
"""

line = 'value one we want; value two, value three,ibex,         foo'
import re
print([x.strip() for x in re.split(r'[;,]', line)])
