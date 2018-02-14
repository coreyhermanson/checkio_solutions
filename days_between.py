import datetime


def days_diff(date1, date2):
    d1 = datetime.datetime(date1[0], date1[1], date1[2])
    d2 = datetime.datetime(date2[0], date2[1], date2[2])
    return abs((d2 - d1).days)
