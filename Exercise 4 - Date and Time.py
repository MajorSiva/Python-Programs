#1. Write a Python script to display the
#a) Current date and time

from datetime import datetime
now = datetime.now()
current_date = datetime.now()
print("Current date:", current_date)

#b) Current year

import datetime

current_datetime = datetime.datetime.now()
current_year = current_datetime.year
print(f"Current Year: {current_year}")

#c) Month of year

import datetime

current_datetime = datetime.datetime.now()
current_month = current_datetime.month
print(f"Current Month: {current_month}")

#d) Week number of the year

import datetime
today = datetime.date.today()
week_number = today.isocalendar()[1]
print("The current ISO week number is:", week_number)

#e) Weekday of the week

import datetime

current_datetime = datetime.datetime.now()
current_week = current_datetime.weekday()
print(f"Current Week: {current_week}")

#f) Day of year

import datetime

day_of_year = datetime.datetime.now().timetuple().tm_yday
print(day_of_year)

#g) Day of the month

import datetime

day_of_year = datetime.datetime.now().timetuple().tm_mday
print(day_of_year)

#h) Day of week

import datetime

day_of_year = datetime.datetime.now().timetuple().tm_wday
print(day_of_year)

#2. Write a Python program to determine whether a given year is a leap year.

import calendar

n= int(input("Enter a Year to check leap year:"))
if calendar.isleap(n) is True:
    print(n,"is a leap year")
else:
    print(n,"is not a leap year")

#3. Write a Python program to convert a string to datetime.

import datetime

date_str = input("Enter a datetime string to convert:")
date_format= "%Y-%m-%d %H:%M:%S"

date_time= datetime.datetime.strptime(date_str,date_format)
print(date_time)

#4. Write a Python program to get the current time in Python.

import datetime
now = datetime.datetime.now()
current_time = now.time()
print("Current time:",current_time)

#5. Write a Python program to subtract five days from current date.

from datetime import date, timedelta

dt = date.today() - timedelta(days=5)
print('Current Date:', date.today())
print('5 days before Current Date:', dt)

#6. Write a Python program to convert unix timestamp string to readable date.

import datetime

print(datetime.datetime.fromtimestamp(int("1284105682")).strftime('%Y-%m-%d %H:%M:%S'))

#7. Write a Python program to print yesterday, today, tomorrow.

from datetime import date, timedelta

dt1 = date.today() - timedelta(days=1)
dt2= date.today()+timedelta(days=1)
print("Yesterday:",dt1)
print("Today:", date.today())
print("Tomorrow:",dt2)
 
#8. Write a Python program to convert the date to datetime (midnight of the date) in Python

from datetime import date
from datetime import datetime

dt=date.today()
print(datetime.combine(dt,datetime.min.time()))

#9. Write a Python program to print next 5 days starting from today.

from datetime import date, timedelta

dt= date.today()+timedelta(days=5)
print("Current Date:",date.today())
print("5 days from Current date:",dt)

#10. Write a Python program to add 5 seconds with the current time

import datetime

now=datetime.datetime.now()
t= now+datetime.timedelta(seconds=5)
print("Current Time:",now.time())
print("Time after 5 seconds:",t.time())

#11. Write a Python program to convert Year/Month/Day to Day of Year in Python.

import datetime

day_of_year = datetime.datetime.now().timetuple().tm_yday
print(day_of_year)

#12. Write a Python program to get current time in milliseconds in Python

from time import time
milliseconds= int(time()*1000)
print("Time in Milliseconds:",milliseconds)

#13. Write a Python program to get week number.

import datetime
today = datetime.date.today()
week_number = today.isocalendar()[1]
print("The current ISO week number is:", week_number)

#14. Write a Python program to find the date of the first Monday of a given week

import time
week_number = 50
year = 2015
date_string = f"{year} {week_number} 1"
first_monday = time.asctime(time.strptime(date_string, '%Y %W %w'))
print(first_monday)

#15. Write a Python program to select all the Sundays of a specified year.

from datetime import date, timedelta

def all_sundays(year):
    dt = date(year, 1, 1)
    dt += timedelta(days=6 - dt.weekday())  
    while dt.year == year:
        yield dt
        dt += timedelta(days=7)

y=int(input("Enter a year :"))
for s in all_sundays(y):
    print(s)

#16. Write a Python program to get days between two dates

from datetime import date

def numOfDays(date1, date2):
    if date2 > date1:
        return (date2 - date1).days
    else:
        return (date1 - date2).days

date1 = date(2024, 5, 15)
date2 = date(2024, 5, 10)
print(numOfDays(date1, date2), "days")

#17. Write a Python program to get the date of the last Tuesday.

from datetime import date, timedelta

today = date.today()
offset = (today.weekday() - 1) % 7
last_tuesday = today - timedelta(days=offset)
print(last_tuesday)

#18. Write a Python program to get the last day of a specified year and month

import datetime,calendar

def last_day_month(year, month):
    input_date = datetime.date(year + int(month / 12), month % 12 + 1, 1) - datetime.timedelta(days=1)
    return input_date

year=int(input("Enter a year:"))
month=int(input("Enter a month:"))
last_day = last_day_month(year, month)
print(f"Last day of {calendar.month_name[month]} {year}: {last_day}")

#19. Write a Python program to get the number of days of a given month and year.

from calendar import monthrange

year= int(input("Enter a year:"))
month= int(input("Enter a month:"))
print("Number of days in",year,month,"is:",monthrange(year,month))

#20. Write a Python program to convert a date to the timestamp.

import time
from datetime import datetime

now= datetime.now()
print(time.mktime(now.timetuple()))

#21. Write a Python program to convert a string date to the timestamp.

import time
from datetime import datetime

string =input("Enter a date:") #"20/01/2020"
print(time.mktime(datetime.strptime(string,"%d/%m/%Y").timetuple()))

#22. Write a Python program to convert two date difference in days, hours, minutes, seconds.

import datetime

date1 = datetime.datetime(2024, 5, 15, 18, 25, 30)
date2 = datetime.datetime(2024, 4, 15, 8, 21, 10)
time_difference = date1 - date2
total_seconds = time_difference.total_seconds()
days, remainder = divmod(total_seconds, 24 * 60 * 60)
hours, remainder = divmod(remainder, 60 * 60)
minutes, seconds = divmod(remainder, 60)

print(f"Days: {int(days)}")
print(f"Hours: {int(hours)}")
print(f"Minutes: {int(minutes)}")
print(f"Seconds: {int(seconds)}")
