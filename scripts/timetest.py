from datetime import timedelta
from typing import Optional

#from pendulum import UTC, Date, DateTime, Time, Local
import pendulum

dt = pendulum.now()
print(dt)
print(dt.month)
print(dt.weekday())

dt = pendulum.now('UTC')
print(dt)
print(dt.month)
print(dt.weekday())


l = pendulum.local(2022, 9, 12)
print(l)
print(l.month)
print(l.weekday())
print(l.timezone.name)


def ordinal_to_int(ordinal) -> int:
    if ordinal == '1st':
        return 1
    elif ordinal == '2nd':
        return 2
    elif ordinal == '3rd':
        return 3
    elif ordinal == '4th':
        return 4
    else:
        raise ValueError("invalid ordinal value. please provide one of '1st', '2nd', '3rd', '4th'")

def dow_to_int(day_of_week) -> int:
    if day_of_week == 'mon':
        return 0
    elif day_of_week == 'tue':
        return 1
    elif day_of_week == 'wed':
        return 2
    elif day_of_week == 'thu':
        return 3
    elif day_of_week == 'fri':
        return 4
    elif day_of_week == 'sat':
        return 5
    elif day_of_week == 'sun':
        return 6
    else:
        raise ValueError("invalid day of week indicator. please provide one of 'mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun'")

def find_next_start_day(last_start: pendulum.datetime, ordinal: int, wkday: int) -> pendulum.datetime:
    print(last_start)
    working_dt = pendulum.datetime(last_start.year, last_start.month, 1).add(months=1)
    print(working_dt)
    n = 0;
    for i in range(1, working_dt.days_in_month):
        print("iteration ", i)
        print(working_dt, " ", working_dt.weekday())
        if working_dt.weekday() == wkday:
            n = n+1
            print(n)
            if n == ordinal:
                return working_dt
        working_dt = working_dt.add(days=1)
    raise ValueError("day of month not found")

nth_day = ordinal_to_int('1st')
print(nth_day)
dow = dow_to_int('wed')
print(dow)

next_start = find_next_start_day(dt, nth_day, dow)

print(next_start)

