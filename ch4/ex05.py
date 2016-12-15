a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

f = open('test.txt')
for line in reversed(list(f)):
    print(line, end='')

class Countdown:
    
    def __init__(self, start):
        self.start = start
   
    def __iter__(self):
       n = self.start
       while n > 0:
           yield n
           n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

c = Countdown(32)

for x in c:
    print(x, end='; ')

print()

for x in reversed(c):
    print(x, end='; ')
