record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])
print("With slices: ", cost)

shares = slice(20,32)
price = slice(40,48)

cost = int(record[shares]) * float(record[price])
print("With named slices: ", cost)
