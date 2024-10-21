# Dates 

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year2024 = datetime(2024, 1, 1)

print_date(year2024)

from datetime import time

current_time = time(18, 59, 24)

print(current_time.hour)
print(current_time.min)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2024, 1, 10)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date.year = date(current_date.year, current_date.month +1 , current_date.day)
print(current_date.month)

from datetime import timedelta

time_delta = timedelta()
