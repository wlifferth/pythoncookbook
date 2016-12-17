# Problem: You want to output data using print() but you also want to change the separator character or line ending

stuff = ['ACME', 50, 91.5]
print(*stuff)
print(*stuff, sep=',')
print(*stuff, sep=',', end='!!\n')

for i in range(5):
    print(i)

for i in range(5):
    print(i, end='')
