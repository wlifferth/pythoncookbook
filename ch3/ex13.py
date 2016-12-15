# Problem: You want a general solution for finding the date for the last occurence of a day of the week. Last friday, for example.

from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def getPreviousDay(dayName, startDate=None):
    if startDate is None:
        startDate = datetime.today()
    dayNum = startDate.weekday()
    dayNumTarget = weekdays.index(dayName)
    daysAgo = (7 + dayNum - dayNumTarget) % 7
    if daysAgo == 0:
        daysAgo = 7
    targetDate = startDate - timedelta(days=daysAgo)
    return targetDate

print(getPreviousDay('Friday'))

# Same thing with dateutil
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
print(d)

# Next Friday
print(d + relativedelta(weekday=FR))

# Last Friday
print(d + relativedelta(weekday=FR(-1)))
