# Problem: You have some code that needs to loop over each date in a current month, and want and efficient way to calculate that date range

from datetime import datetime, date, timedelta
import calendar

def getMonthRange(startDate=None):
    if startDate is None:
        startDate = date.today().replace(day=1)
    _, daysInMonth = calendar.monthrange(startDate.year, startDate.month)
    endDate = startDate + timedelta(days=daysInMonth)
    return (startDate, endDate)

aDay = timedelta(days=1)

first, last = getMonthRange()

while first < last:
    print(first)
    first += aDay
