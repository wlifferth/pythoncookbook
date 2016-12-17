# Problem: You need to read or write text data, possibly in different text encodings such as ASCII, UTF-8, or UTF-16

with open('test.txt', 'rt') as f:
    data = f.read()
    print(data)

with open('test.txt', 'rt') as f:
    for line in f:
        print(line, end='\b*')

with open('out.txt', 'wt') as f:
    f.write(data)

with open('out.txt', 'wt') as f:
    print("Hey there line 1", file=f)
    print("Hey there line 2", file=f)
    print("Hey there line 3", file=f)

# Using the with keyword allows us to now worry about closing a file

f = open('test.txt', 'rt', encoding='ascii', errors='replace')
print(f.read())
g = open('test.txt', 'rt', encoding='ascii', errors='ignore')
print(g.read())
