"""
Problem: You have code that accesses list or tuple elements by position, but this makes the code somehwat difficult to read at times. You'd also like to be less dependent on position in the structure, accessing the element by name
"""
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('wlifferth@icloud.com', '2016-12-7')
print(sub)
print(sub.addr)
print(sub.joined)
print("len(sub):", len(sub))

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * r.price
    return total

records = [
        ['APPL', 57, 213.45],
        ['O', 400, 6.22],
        ['VZW', 20, 89.12]
        ]

print(cost(records))
