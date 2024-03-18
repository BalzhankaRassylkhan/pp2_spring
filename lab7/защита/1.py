class jimin:   
    def sumof(self):
        n = int(input())
        a = []
        sum = 0
        for i in range(n):
            b = int(input())
            a.append(b)
            sum += b
        print(sum)

s = jimin()
s.sumof()