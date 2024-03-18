def balzhan(n):
    for i in range(0,101):
        if i%5==0:
            yield i
n = int(input())
v = balzhan(n)
print(*v,sep=", ")
