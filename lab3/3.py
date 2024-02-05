heads, legs= map(int, input().split())


def solve(a,b):
    rabbits, chickens = 0, 0
    for i in range(a):
        if (i*2)+((a-i)*4) == b:
            chickens = i
            rabbits = a-i
    return chickens, rabbits

nc, nr =  solve(heads, legs)

print("Chickens:", nc) 
print("Rabbits:", nr)