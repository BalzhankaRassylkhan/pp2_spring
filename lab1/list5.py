list = ["asd", "qwerty", "ball"]
list.insert(2, "uni")
print(list)
letter=['h','g','t']
list.extend(letter)
print(list)
list.remove("asd")
print(list)
del list[2]
print(list)

list.clear()

print(list)
thislist = ["aruzhan", "balzhan", "aisha"]
for i in range(len(thislist)):
  print(thislist[i])