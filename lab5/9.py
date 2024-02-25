import re

def test(pattern, testData, testNumber, expectedResult):
    result = re.sub(pattern, r"\1 \2", testData)
    print(result)
    if result == expectedResult:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")

pattern = r'(\w)([A-Z])'
test(pattern, "MyNameIsAnton", "test1", "My Name Is Anton")