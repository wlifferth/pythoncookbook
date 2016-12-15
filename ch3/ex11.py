# Problem: You want to pick random items out of a sequence or generate random numbers

import random
print(format("Random Choice", '•^30'))
values = [1, 2, 3, 4, 5, 6]
print("random.choice(values):")
for x in range(4):
    print(random.choice(values))

print(format("Random Sample", '•^30'))
print("random.sample(values, 4)")
for x in range(4):
    print(random.sample(values, 4))

print(format("Random Values", '•^30'))
print("Values: {}".format(values))
random.shuffle(values)
print("Values: {}".format(values))
random.shuffle(values)
print("Values: {}".format(values))

print(format("Random Integers", '•^30'))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))

print(format("Random Float (0, 1)", '•^30'))
print(random.random())
print(random.random())
print(random.random())

print(format("Random Bits", '•^30'))
print(random.getrandbits(200))

print(random.randint(0, 100))
random.seed()
print(random.randint(0, 100))
