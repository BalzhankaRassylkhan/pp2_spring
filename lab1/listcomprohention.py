list=["bal","uip","asd","dada","asddf"]
newlist=[]
for x in list:
    if "d" in x:
        newlist.append(x)
print(newlist)    

colors = ["awhite", "red", "yellow", "black", "purpil"]

newlist = [x if x != "black" else "red" for x in colors]

print(newlist)