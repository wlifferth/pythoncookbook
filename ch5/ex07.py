# Problem: You need to read or write data in a file with gzip or bz2 compression

# Solution: The gzip and bz2 modules make it easy to work with compressed files. Basically they both have alternative versionsn of open() that can be used with different files.

import gzip
with gzip.open('test.txt.gz', 'rt') as f:
    print(f.read())
