# Problem: You want to write data to a file, but only if it doesn't already exist on the filesystem

# Solution: Use the x mode to open() instead of the w mode
# with open('xyz.txt', 'xt') as f:
#    f.write("Hello there")

import os
if not os.path.exists('xyz.txt'):
    with open('somefile', 'wt') as f:
        f.write('Hello there')
else:
    print("File already exists doofus!")
