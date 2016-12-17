# Problem: You want to iterate over a sequence, but would like to keep track of which element of the sequence is currently being processed.

my_list = ['a', 'b', 'c']

for index, val in enumerate(my_list, 1):
    print(index, val)

def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except:
                print('Line {}: Parse error: {}'.format(lineno, line))

parse_data('ex10.txt')

from collections import defaultdict
word_summary = defaultdict(list)

with open('test.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    # Create a list of words in the current line
    words = [w.strip().lower for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)
