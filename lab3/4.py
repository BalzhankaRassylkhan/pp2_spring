def isprime(a):
    cnt=0
    for i in range(1,a+1):
        if a% i ==0:
            cnt = cnt +1
    return cnt ==2

def filter(b):
    result=[]
    for a in b:
        if isprime(a):
            result.append()
    return result

b=list(map(int,input().split()))
print(filter(b))

       