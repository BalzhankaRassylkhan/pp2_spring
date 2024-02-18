def divided_3_4(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i

x=int(input())
a=divided_3_4(x)
print(*a,sep=", ")