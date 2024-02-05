b=[]
a=int(input())

for i in range(a):
    x= int(input())
    b.append(x)
def has_33(b):
    a=len(b) 
    for i in range(a-1):
        if b[i]==3 and b[i]==3:
            return True
    return False
print(has_33(b))
