"""
Problem: You want to replace HTML or XML entities such as &entity; or &#code; with their corresponding text. Alternatively you need to produce text, but escape certain chars (e.g. <, >, or &)
"""

s = "Elements are written as '<tag>text</tag>'."
import html
print(s)
print(html.escape(s))

# Disable escaping of quotes
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))
