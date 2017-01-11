# Problem: You want to read or write data encoded as a csv file

# Solution: For most kind of csv data, use the csv library

import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(*["{:10}".format(header) for header in headers], sep='')
    for r in f_csv:
        print(*["{:10}".format(item) for item in r], sep='')

# Same deal with named tuples

from collections import namedtuple
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(*["{:10}".format(header) for header in headers], sep='')
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        print("{:10}{:10}{:10}{:10}{:10}{:10}".format(row.Symbol, row.Price, row.Date, row.Time, row.Change, row.Volume))

with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)

headers = ['ColumnA', 'ColumnB', 'ColumnC', 'Total']
rows = [[a, a+1, a+2, (a*3 + 3)] for a in range(0,20,3)]
with open('data.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

dict_rows = [{'ColumnA': a, 'ColumnB': a+1, 'ColumnC': a+2, 'Total': (a*3 +3)} for a in range(0, 20, 3)]
print("\n\nDict print\n\n")
print(dict_rows)
print("\n\nDict pprint\n\n")
from pprint import pprint
pprint(dict_rows)

with open('data.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(dict_rows)
