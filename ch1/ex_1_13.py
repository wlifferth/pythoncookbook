"""
Problem: You have a list of dictionaries and you would like to sort the entries according to one or more of the dictionary values
"""

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
    {'fname': 'Ara', 'lname': 'Jones', 'uid': 1005}
] 

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print("\n")
print(rows_by_uid)
print("\n")

rows_by_lname_fname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lname_fname)
