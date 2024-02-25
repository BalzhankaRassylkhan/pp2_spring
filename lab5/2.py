import re
def match_s(string):

    pattern = r"ab{2,3}"
    return bool(re.search(pattern,string))


strings = ['aaabbb', 'sabb', 'ajs', 'abaab', 'x', 'aabbas']

for string in strings:
    if match_s(string):
        print(f"{string} is OK!")
    else:
        print(f"{string} NO!")