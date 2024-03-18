import re
def  validate_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+[a-zA-Z{2,}]$'
    return re.match(pattern,email)is not None

email = input("ВВеди имеил:")
if validate_email(email):
    print("Email адрес правильный")
else:
    print("EMail адрес не правильный")