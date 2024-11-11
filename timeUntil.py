#! python.exe

# timeUntil.py - Returns a string with the amount of time between now and the provided date.
# Or amount of time that has passed if the date is in the past.

import datetime, time, sys

currentDate = datetime.datetime.fromtimestamp(time.time())

try:
    targetDate = datetime.datetime.strptime(" ".join(sys.argv[1:]), '%d %B %Y')
except Exception as e:
    print(f'Error: {e}')
    print('Usage: 01 January 2024')


print(f'Current Date: {currentDate.strftime('%d-%B-%Y')}')

if targetDate > currentDate:
    timeBetween = targetDate - currentDate
    print(f'There are {timeBetween.days} days between now and {targetDate.strftime('%d-%B-%Y')}')
else:
    timeBetween = currentDate - targetDate
    print(f'There has been {timeBetween.days} days since {targetDate.strftime('%d-%B-%Y')}')