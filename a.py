x = int(input())
y = int(input())
c = (x + y + abs(x - y)) / 2
c = int(c)
soma = 0

if(x > y):
    d = int(y)
else: d = int(x)

for i in range(d, c + 1):
    if(i % 13 != 0):
        soma  = soma + i
print(soma)
