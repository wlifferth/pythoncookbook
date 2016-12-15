# Problem: You want to take a slice of data produced by an iterator, but the normal slicing operator doesn't work

def count(n):
    while True:
        yield n
        n += 1

c = count(0)
import itertools
for x in itertools.islice(c, 10, 20):
    print(x)
