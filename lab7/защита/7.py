import math
def  digit_gen():
    str_pi =str(math.pi).replace(".","")
    for digit in str_pi:
        yield int(digit)

def get_pi_digit(n):
    gen = digit_gen()
    for i  in range (n):
        digit = next(gen)
    return digit

n = int(input())
pi = get_pi_digit(n)
print(f"Цифра числа ПИ под индексом {n}:{pi}")