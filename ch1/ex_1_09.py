a = {
        'x' : 1,
        'y' : 2,
        'z' : 3 
        }

b = {
        'w': 10,
        'x': 11,
        'y': 2
        }
print("Keys in a and b")
print(a.keys() & b.keys())

print("Keys in a and not in b")
print(a.keys() - b.keys())

print("Vals in a and b")
print(set(a.values()) & set(b.values()))

print("Entries in a and b")
print(a.items() & b.items())
