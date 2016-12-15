"""
Problem: You need to format text with some sort of alignment applied
"""

text = "Hello World"
print(text)
print(text.ljust(20, "•"))
print(text.rjust(20, "•"))
print(text.center(20, "•"))

print(format(text, '<20'))
print(format(text, '>20'))
print(format(text, '^20'))

print(format(text, '+<20'))
print(format(text, '+>20'))
print(format(text, '+^20'))

number = 3.141592
print(format(number, '>20.2f'))
print(format(number, '^20.4f'))
