import datetime
x=datetime.datetime.now()
y= x - datetime.timedelta(days=1)
z= x + datetime.timedelta(days = 1)
print("Yesterday:",y.strftime("%B,%d"))
print("Today:",x.strftime("%B,%d"))
print("Tomorrow:",z.strftime("%B,%d"))