a=['ban',"zhan","hjk"]
b=[788,9,5,6]
c=a+b
print(c)

for x in b:
    a.append(x)
print(a)

b.extend(a)
print(b)