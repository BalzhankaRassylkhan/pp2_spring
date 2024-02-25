import re
snake = input()
def snaketocamel(snake):
    camel = re.sub(r"_+"," ",snake).lower()
    camel = " ".join(word.capitalize() or"_" for word in camel.split())
    return camel

camel = snaketocamel(snake)
print(camel)