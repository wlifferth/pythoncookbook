prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
        }

print("MAX (of dict) ", min(prices))
print("MIN (of dict) ", max(prices))


min_price = min(zip(prices.values(), prices.keys()))
print("MIN", min_price)
max_price = max(zip(prices.values(), prices.keys()))
print("MAX", max_price)

sbp = list(zip(prices.values(), prices.keys()))
print("Min:", min(sbp))
print("Max:", max(sbp))
