import math
def gen_pi(n):
    return f"{math.pi:.{n}f}"

n = int(input())
print(gen_pi(n))