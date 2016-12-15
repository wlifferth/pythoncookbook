"""
Problem: You want to match a block of text using a regular expression, but you need the match to span multiple lines
"""
import re

comment = re.compile(r'/\*(.*?)\*/')
a = '/* this is a comment */'
b = '''/* this is a multiline comment
and it spans multiple line
linke a multiline comment might do */'''

print(comment.findall(a))
print(comment.findall(b))


comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(a))
print(comment.findall(b))
