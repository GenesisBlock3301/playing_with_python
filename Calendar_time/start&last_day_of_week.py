import datetime
import time
import calendar


def find_start_ending_day_of_week(year, week):
    print("Year and Week", year, week)
    first_day_of_week = datetime.datetime.strptime(f"{year}-W{int(week)}-1", '%Y-W%W-%w').date()
    last_day_of_week = first_day_of_week + datetime.timedelta(days=6.9)
    return first_day_of_week, last_day_of_week


my_date = datetime.date.today()
year, week, day_of_week = my_date.isocalendar()
first_day, last_day = find_start_ending_day_of_week(year, week - 1)
# print(" ".join(str(first_day).split("-")[::-1]), last_day)
dic = dict()
for single_date in (first_day + datetime.timedelta(n) for n in range(7)):
    date = " ".join(str(single_date).split("-")[::-1])
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    dic[calendar.day_name[day]] = single_date
    print(calendar.day_name[day], single_date)

print(dic)
