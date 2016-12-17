# Problem: You need to perform the same operation on many objects, but the objects are contained in different containers, and you'd like to avoid nested loops without losing the readability of your code.

from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

active_items = set(['Kanye West', 'Stephen Hawking', 'Mitt Romney'])
inactive_items = set(['Amadeus Mozart', 'Marie Curie', 'Theodore Roosevelt'])
for item in chain(active_items, inactive_items):
    print("{} was a real person".format(item))


