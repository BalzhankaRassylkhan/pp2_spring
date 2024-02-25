import re
string = input()

def balzhan(string):
    pattern = r"\s|\,|\."
    return re.sub(pattern,":",string)
result = balzhan(string)
print(result)


