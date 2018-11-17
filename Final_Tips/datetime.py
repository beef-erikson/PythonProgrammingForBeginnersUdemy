"""Examples using the datetime module.
"""

import datetime

# Today's date
today = datetime.datetime.today()
print(datetime.datetime.today())
print(f'Day: {today.day} Month: {today.month} Year: {today.year}')

# Makes a new date
some_date = datetime.datetime(2018, 11, 17)
print(some_date)

# Manipulating date values - adds 90 days
day = some_date
day + datetime.timedelta(day=90)
