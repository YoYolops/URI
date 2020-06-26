X = int(input())
Y = int(input())
x = int(max(X, Y))
y = int(min(X, Y))
num = []
for i in range(y + 1, x):
    if((i % 5 == 2) or (i % 5 == 3)):
        num.append(i)
sorted(num, key = int)

for i in num:
    print(i)
