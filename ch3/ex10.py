# Problem: You need to perform matrix and linear algebra operations, such as matrix multiplication, finding determinants, solving linear equations, and so on.

import numpy as np

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)

# Return transpose
print(m.T)

# Return inverse
print(m.I)

# Create a vector and multiply
v = np.matrix([2, 3, 4]).T
print(m * v)

import numpy.linalg as linalg

# Determinant
print(linalg.det(m))

# Eigenvalues
print(linalg.eigvals(m))

# Solve for x in mx = v
x = linalg.solve(m, v)
print(x)
