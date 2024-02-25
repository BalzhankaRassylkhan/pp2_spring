import re

pattern = re.compile('ab*')

test_strings = ['aaaab', 's', 'ajs', 'abaa', 'x', 'aabbas']

for test_string in test_strings:
    if pattern.match(test_string):
        print(f"{test_string} is passed!")
    else:
        print(f"{test_string} is not passed!")