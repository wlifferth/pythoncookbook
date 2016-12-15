"""
Problem: You need to format a number for output, controlling the number of digits, alignment, inclusion of a thousands seperator, and other details
"""

x = 1234.56789
# Two decimal places of accuracy
print(format(x, '0.2f'))

# Right justified in 10 spaces, one digit accuracy
print(format(x, '>10.1f'))

# Centered
print(format(x, '•^12.1f'))

# Inclusion of thousands seperator
print(format(x, ','))

# the general form of the formatter string [<>^]?width[,]?(.dig its)?
