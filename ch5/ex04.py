# Problem: You need to read or write binary data, such as that found in images, sounds files, and so on.
# Solution: Use the open() function with mode rb or wb to read or write

# Read entire file as a single byte string
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello world')

with open('somefile.bin', 'rb') as f:
    data = f.read()

t = 'Hello'
print(t[0])
for c in t:
    print(c, end=' ')

# When you index or iterate over a byte value, you'll get byte-integers
b = b'Hello'
print(b[0])
for c in b:
    print(c, end=' ')

with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
    print(text)

import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin', 'wb') as f:
    f.write(nums)
