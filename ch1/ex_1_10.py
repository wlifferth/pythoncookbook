
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupeDict(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [4, 2, 6, 2, 5, 4, 1, 6, 2]

print("Before: ", a)

a = list(dedupe(a))

print("After: ", a)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

print("Before: ", a)

a = list(dedupeDict(a, key=lambda s: (s['x'], s['y'])))

print("After: ", a)
