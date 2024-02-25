import re
String = "When you Wake up in the Morning, think about the Precious Privilege of being Alive again - to breathe, to_think, to enjoy and to love."
def balzhan(String):
    return re.findall(r"[A-Z][a-z]*",String)

result = balzhan(String)
print(result)
