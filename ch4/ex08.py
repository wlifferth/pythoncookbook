# Problem: You want to iterate over items in an iterable, but the first few items aren't of interest and you just wnat to discard them

with open('test.txt') as f:
    for line in f:
        print(line, end='')

print("\n\nPrinting the same thing, only cutting off the lines with #\n")

from itertools import dropwhile
with open('test.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

from itertools import islice
items = ['1', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)
