"""
Problem: You have long strings that you want to reformat so that they fill a user-specified number of columns
"""

s = "Go placidly amid the noise and haste, and remember what peace there may be in silence. As far as possible without surrender, be on good terms with all persons.\n"

import textwrap
print(textwrap.fill(s, 70))
print()
print(textwrap.fill(s, 40))
print()
print(textwrap.fill(s, 40, initial_indent='\t'))
print()
print(textwrap.fill(s, 40, subsequent_indent='\t'))
