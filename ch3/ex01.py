"""
Problem: You want to rounda  floating-point number to a fixed number of decimal places
"""

pi = 3.14159265
print("{} -> {}".format(pi, round(pi, 1)))
print("{} -> {}".format(pi, round(pi, 4)))
x = 1.43
print("{} -> {}".format(x, round(x, 1)))
x = 1.47
print("{} -> {}".format(x, round(x, 1)))
x = 6174
print("{} -> {}".format(x, round(x, -1)))
print("{} -> {}".format(x, round(x, -2)))
