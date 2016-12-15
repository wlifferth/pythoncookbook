from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['a'].append(2)
d['b'].append(4)

print(d)

s = defaultdict(set)

s['a'].add(1)
s['a'].add(2)
s['a'].add(2)
s['b'].add(4)

print(s)
