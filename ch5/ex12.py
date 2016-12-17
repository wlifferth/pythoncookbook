# Problem: You need to test whether or not a file or directory exists

# Solution: Use the os.path module to test for the existence of a file or directory

from os import path

a = '/etc/passwd'
b = '/tmp/spam'

print(a, "exists?", path.exists(a))
print(b, "exists?", path.exists(b))

print(a, "is a regular file?", path.isfile(a))
print(a, "is a directory?", path.isdir(a))
print(b, "is a symbolic link?", path.islink(b))
print(a, "size?", path.size(a))
print(a, "last modified?", path.getmtime(a))
