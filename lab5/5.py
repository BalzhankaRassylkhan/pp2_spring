import re

string = input()
pattern = r"a.*b$"
balzhan = re.search(pattern,string)


if balzhan:
    print("OK")
else:
    print("NO")