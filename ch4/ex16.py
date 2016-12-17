# Problem: You have code that uses a while loop to iteratively process data because it involves a function or some kind of unusual test condition that doesn't fall into the usual iteration pattern.

import sys
f = open('test.txt')
for chunk in iter(lambda: f.read(2), ''):
    n = sys.stdout.write(chunk)
