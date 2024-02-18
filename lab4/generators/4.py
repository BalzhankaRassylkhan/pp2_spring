def squares(n):
    for i in range(a,b+1):
        yield i**2

a = int(input())
b = int(input())
x=squares(a)
x=squares(b)
print(*x)