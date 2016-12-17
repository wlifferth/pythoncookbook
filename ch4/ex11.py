# Problem: You want to iterate over the items contained in more than one sequence at a time

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, "\t", y)


a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']

for i in zip(a, b):
    print(i)


from itertools import zip_longest

print("With zip_longest")
for i in zip_longest(a, b):
    print(i)


print("With zip_longest and fillvalue=0")
for i in zip_longest(a, b, fillvalue=0):
    print(i)


headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
print(s)

a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)

print(zip(a, b))
print(list(zip(a, b)))
