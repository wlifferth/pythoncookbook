# Problem: You need to perform calculations on large numerical datasets, such as arrays or grids

# Python list
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print('{} * 2 = {}'.format(x, x * 2))
print('{} + {} = {}'.format(x, y, x + y))

# Numpy arrays
import numpy as np
ax = np.array(x)
ay = np.array(y)
print('{} * 2 = {}'.format(ax, ax * 2))
print('{} * {} = {}'.format(ax, ay, ax * ay))

def f(x):
    return 3*x**2 - 2*x + 7

print(f(ax))

grid = np.zeros(shape=(10000, 10000), dtype=float)
print(grid)
# grid += 10
print(grid)
# print(np.sin(grid))

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a)
print(a[1])
print(a[:,1])

# Pick a subregion of the array and update it
print(a[1:3,1:3])
a[1:3,1:3] += 10
print(a)

# Apply addition of a row vector across all rows
print(a + [100, 101, 102, 103])

# Selecting only cells where a < 10, otherwise -1
print(np.where(a < 10, a, -1))
