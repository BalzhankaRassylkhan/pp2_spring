def square(n):
    for i in range(n):
        yield i ** 2

n = int(input())
for x in square(n):
    print(x)