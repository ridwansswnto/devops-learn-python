from datetime import datetime
from os import getcwd

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

right_this_minute = datetime.today().minute
day_now = datetime.today().day
print(right_this_minute)
print(day_now)

if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not and odd minute")

where_am_i = getcwd()
print("=" * 10)
print(where_am_i)