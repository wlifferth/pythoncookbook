# Problem: You want to iterator over all the possible combinations or permutations of a collection of items.

items = ['a', 'b', 'c']
from itertools import permutations
print("All permutations of {}:".format(items))
for p in permutations(items):
    print(p)

print("All permutations of {} of size 2:".format(items))
for p in permutations(items, 2):
    print(p)

from itertools import combinations
print("All combinations of {} of size 3:".format(items))
for c in combinations(items, 3):
    print(c)

print("All combinations of {} of size 2:".format(items))
for c in combinations(items, 2):
    print(c)
from itertools import combinations_with_replacement
print("All combinations with replacement of {} of size 3:".format(items))
for c in combinations_with_replacement(items, 3):
    print(c)
