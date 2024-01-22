def my(n):
  return abs(n - 56)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = my)
print(thislist)
mylist=['nm','jkl','Asd','Ert']
mylist.sort(key = str.lower)

print(mylist)
mylist.reverse()
print(mylist)