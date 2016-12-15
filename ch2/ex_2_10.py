"""
Problem: You are using regular expressions to process text, but are concerned about the handling of Unicode characters
"""

import re
num = re.compile('\d+')
## ASCII digits
asciidigits = '123'
print(asciidigits)
print(num.match(asciidigits))

## Arabic digits
arabicdigits = '\u0661\u0662\u0663'
print(arabicdigits)
print(num.match(arabicdigits))

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(s)
print(pat.match(s))

print(s.upper())
print(pat.match(s.upper()))
