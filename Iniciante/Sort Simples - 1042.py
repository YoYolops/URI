a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

leitura = [a,b,c]
ordem = sorted(leitura)

for j in ordem:
    print(j)

print()

for i in leitura:
    print(i)