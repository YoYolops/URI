e = int(input())
c0 = 0
c1 = 0
a = list(map(int, input().split()))

for i in range(e):
    if a[i] == 1:
        c1 += 1
    else:
        c0 += 1
if c1 >= c0:
    print("N")
else:
    print("Y")
