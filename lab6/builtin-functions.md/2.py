s = input()
countUpper = sum(1 for x in s if x.isupper())
countSlower = sum(1 for y in s if y.islower())
print(countUpper, countSlower)