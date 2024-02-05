n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
def histogram(numb):
    for num in numb:
        print('*' * num)

histogram(a)