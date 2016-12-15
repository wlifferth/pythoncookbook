filename = 'spam.txt'
print("File ends with '.txt': ", filename.endswith('.txt'))
print("FIle start with 'file': ", filename.startswith('.txt'))
url = 'http://www.python.org'
print("URL starts with 'http': ", url.startswith('http'))

import os

filenames = os.listdir('.')
print("Files:\n", filenames)
print([name for name in filenames if name.endswith(('.txt', '.py'))])

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


