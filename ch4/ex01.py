# Problem: You need to process items in an iterable, but for whatever reason you can't or don't want to use a for loop

with open('test.txt') as x:
    try:
        while True:
            n = next(x)
            print(n, end='')
    except StopIteration:
        pass
