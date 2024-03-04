with open("file1", 'w') as s1:
    s1.write("This is txt for first file")

with open("file1", 'r') as s1:
    print(s1.readline())


with open("file2", 'w') as s2:
    with open("file1", 'r') as s1:
        for line in s1:
            s2.write(line)

with open("file2", 'r') as s2:
    print(s2.readline())