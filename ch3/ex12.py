# You have code that needs to perform simple time conversions, like days to seconds, hours to minutes, and so on.

from datetime import timedelta, datetime

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)

a = datetime(2012, 9, 23)
print(a + timedelta(days=10))

now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

b = datetime(2012, 12, 21)
d = b - a
print(d)
