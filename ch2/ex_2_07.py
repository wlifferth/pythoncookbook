"""
Problem: You're trying to match a text patter with regular expressions, but its identifying the longest possible matches of a pattern. You want it to find the shortest possible match.
"""
import re

a = 'Computer says "no." Phone says "yes."'

# Greedy *
strPat = re.compile(r'\"(.*)\"')
print(strPat.findall(a))

# Non-Greedy *?
strPat = re.compile(r'\"(.*?)\"')
a = 'Computer says "no." Phone says "yes."'
print(strPat.findall(a))
