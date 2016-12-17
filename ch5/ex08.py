# Problem: Instead of iterating over a file by lines, you want to iterate over a collection of fixed sized records or chunks

# Solution: Use iter() and functools.partial()

from functools import partial

RECORD_SIZE = 32

with open('test.txt.gz', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r, "***")
