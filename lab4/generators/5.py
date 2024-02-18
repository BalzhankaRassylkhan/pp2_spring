def tozero(n):
    while n != -1:
        yield n
        n = n-1


n = int(input())
result = tozero(n)
for i in result:
    print(i)