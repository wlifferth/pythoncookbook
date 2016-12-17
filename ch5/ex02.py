# Problem: You want to redirect the output of the print() function to a file

with open('out.txt', 'wt') as f:
    print("Hello world!", file=f)
