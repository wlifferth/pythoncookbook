from collections import OrderedDict

d = dict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

print("Regular Dict\n")
for key in d:
    print(key, d[key])

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

print("\n\nOrdered Dict\n")
for key in d:
    print(key, d[key])
