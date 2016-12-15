"""
Problem: You need to search for and possibly replace text in a case-insensitive manner
Solution: Use the re module, passing the re.IGNORECASE flag to various operations
"""

import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
