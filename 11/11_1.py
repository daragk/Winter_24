import calendar
from datetime import date

thursdays = 0
cur_year = date.today().year

for i in range(1, 13):
    for j in range(1, calendar.monthrange(2024, i)[1] + 1):
        thr = calendar.weekday(cur_year, i, j)
        if thr == 3:
            thursdays += 1
            if thursdays == 3:
                print(date(cur_year, i, j))
    thursdays = 0
