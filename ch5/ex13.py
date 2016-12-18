# Problem: You want to get a list of the files contained in a directory of the filesystem

# Solution: Use the os.listdir() function

import os
names = [name for name in os.listdir('/') if os.path.isfile(os.path.join('/', name))]
print(names)
names = [name for name in os.listdir('/') if os.path.isdir(os.path.join('/', name))]
pyfiles = [name for name in os.listdir('/') if name.endswith('.py')]
print(pyfiles)

import glob
pyfiles = glob.glob('~/*.py')
print(pyfiles)
