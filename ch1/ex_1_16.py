"""
Problem: You have data inside a sequence, and need to extract values or reduce the sequence using some criteria
"""

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([x for x in mylist if x > 0])

print([x ** 0.5 for x in mylist if x > 0])

print([x ** 0.5 if x > 0 else 0 for x in mylist])
