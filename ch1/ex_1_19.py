"""
You need to execute a data reduction (sum(), min(), max(), etc) but first need to transform or filter data
"""


nums = range(0, 20)
s = sum(x * x for x in nums)
print("Sum: ", s)

import os
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print("There's a python script in this directory!")
else:
    print("Sorry... no python.")



