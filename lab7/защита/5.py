def jm(n):
    for i in range(1,n+1):
        yield i**2

n = int(input())
a = jm(n)
for i in a:
    print(i)