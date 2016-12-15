# Your application recieves temporal data in string format, but you want to convert those strings into datetime objects in order to perform nonstring operations on them

from datetime import datetime

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)
