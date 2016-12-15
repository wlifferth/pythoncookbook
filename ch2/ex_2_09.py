"""
Problem: You're working with Unicode strings, but need to make sure that all of the strings ahve the same underlying representation
"""

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1, "==", s2, ":", s1 == s2)
print("len of", s1, ":", len(s1))
print("len of", s2, ":", len(s2))

import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1, "==", t2, ":", t1 == t2)
print(ascii(t1))

