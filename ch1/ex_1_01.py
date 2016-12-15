def section(x):
    if x > 0:
        print("\n")
    print("=" * 10)
    print("section ", x)
    print("=" * 10)

section(0)
p = (4, 5)
print("p: ", p)
x, y = p
print("x, y = p")
print("x: ", x)
print("y: ", y)

section(1)
data = ['ACME', 92.51, 6200]
print("data: ", data)
ticker, price, quantity = data
print("ticker, price, quantity = data")
print("ticker: ", ticker)
print("price: ", price)
print("quantity: ", quantity)

