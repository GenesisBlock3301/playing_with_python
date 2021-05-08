import datetime

my_date = datetime.date.today()
# print(my_date.isocalendar())
year, week_number, day_of_week = my_date.isocalendar()
print(year, week_number, day_of_week)
