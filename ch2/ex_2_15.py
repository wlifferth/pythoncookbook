"""
Problem: You want to create a string in which embedded variable names are substituted with a string representation of a variable's name
"""
s = "{name} has {n} messages"
print(s.format(name="William", n=64))

name = "William"
n = 64
print(s.format_map(vars()))

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('William', n=64)
print(s.format_map(vars(a)))

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
print(s.format_map(safesub(vars())))

import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'William'
n = 64
print(sub('Hello {name}'))
print(sub('You have {n} messages'))
