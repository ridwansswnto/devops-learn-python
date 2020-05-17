from datetime import datetime
from os import getcwd

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

right_this_minute = datetime.today().minute
day_now = datetime.now()
print(right_this_minute)
print("=" * 7)
name_day = day_now.strftime("%A")

if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not and odd minute")

if name_day == "Saturday":
    print("Today is", name_day, ". Jadiiii")
    print("Lets go to holiday! Yeayyy!!!")
elif name_day == "Sunday":
    print("Today is", name_day, ". Jaddiiii")
    print("Lets take a rest, for use to the next day!!!")
else:
    print("Today is", name_day, ". jadiiii")
    print("Ganbatteee!!! hari masih panjang !!!")