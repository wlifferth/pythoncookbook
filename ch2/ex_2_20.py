"""
Problem: You want to perform common text operations (stripping, searching, replacement) on byte strings
"""

data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))
