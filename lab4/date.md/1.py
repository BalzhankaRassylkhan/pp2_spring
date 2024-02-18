import datetime
x = datetime.datetime.now()
y=x - datetime.timedelta( days=5)
print(x.strftime("%Y,%B,%d"))
print(y)