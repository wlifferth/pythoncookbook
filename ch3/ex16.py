# You had a conference call scheduled for December 21, 2012 at 9:30 a.m. in Chicago. At what local time did your friend in Bangalore, India, have to show up to attend?

from datetime import datetime
from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

central = timezone('US/Central')
localDate = central.localize(d)
print(localDate)

bangaloreDate = localDate.astimezone(timezone('Asia/Kolkata'))
print(bangaloreDate)
