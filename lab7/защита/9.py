import re
def balzhan(numb):
    pattern = r'^\+770\d(9)$'
    if re.match(pattern,numb):
        return True
    else:
        return False

numb = "+77073087954"
if balzhan(numb):
    print("YES")
else:
    print("NO")