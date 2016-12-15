import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # prints the 3 largest elements in nums; in this case [42, 37, 23]
print(heapq.nsmallest(3, nums)) # prints the 3 smallest elements in nums; in this case [-4, 1, 2]

print("=" * 20, "\n")

portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.2},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
        ]

first = [x['name'] for x in heapq.nsmallest(3, portfolio, key=lambda s: s['name'])]
print("First: {}".format(first))
last = [x['name'] for x in heapq.nlargest(3, portfolio, key=lambda s: s['name'])]
print("Last: {}".format(last))

cheap = [x['name'] for x in heapq.nsmallest(3, portfolio, key=lambda s: s['price'])]
print("Cheap: {}".format(cheap))
expensive = [x['name'] for x in heapq.nlargest(3, portfolio, key=lambda s: s['price'])]
print("Expensive: {}".format(expensive))
