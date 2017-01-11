# Problem: You would like to extract data from a simple XML document

# Solution: The xml.etree.ElementTree module can be used to extract data from simple XML documents.

from urllib.request import urlopen
from xml.etree.ElementTree import parse

u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

from itertools import islice
for item in islice(doc.iterfind('channel/item'), 5):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()
