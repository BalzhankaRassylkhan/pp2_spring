from datetime import datetime

def difference(date1, date2):
    dt1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    diff = dt2 - dt1
    return diff.total_seconds()

date1 = "2022-01-01 16:00:30"
date2 = "2022-01-02 12:00:00"

print("Разница в секундах:", difference(date1, date2))