x = int(input())
n = 1
y = int((x*2)/2)

for i in range(y):
    print("%d %d %d"%(n, pow(n,2), pow(n,3)))
    print("%d %d %d"%(n, pow(n,2)+1,pow(n,3)+1))
    n = n + 1
