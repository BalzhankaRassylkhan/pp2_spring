import os

c = os.getcwd()
m =[]
d =[]

with os.scandir(c) as it:
    for entry in it:
        if entry.is_dir():
            m.append(entry)

it = os.scandir(c)
for enrty in it:
    if not enrty.is_dir():
        d.append(entry)

print(m)
print(d)
print(c)