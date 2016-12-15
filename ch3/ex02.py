"""
Problem: You need to perform accurate calculations with decimal numbers, and don't want the small errors that naturally occur with floats
"""

from decimal import Decimal, localcontext
ab = 5.2
bb = 2.1
print("{} + {} = {}".format(ab, bb, ab + bb))
a = Decimal('5.2')
b = Decimal('2.1')
print("{} + {} = {}".format(a, b, a + b))

print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

nums = [1.23e+18, 2, -1.23e+18]
# When we print the sum, the 2 in nums will dissappear
print(sum(nums))
# This kind of error can be avoided by using math.fsum:
import math
print(math.fsum(nums))
