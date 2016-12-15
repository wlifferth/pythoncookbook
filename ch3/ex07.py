# Problem: You need to create or test for the floating-point values of infinity, negative infinity, or NaN (not a number)
import math

a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c, sep='; ')

print(math.isinf(a))
print(math.isnan(c))
