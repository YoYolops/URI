e = int(input())
a = []
c = 0
lista = []
for i in range(e):
    numero = int(input())
    lista.append(numero)
    if numero not in a:
        a.append(numero)
a = sorted(a)

while c < len(a):
    print("%d aparece %d vez(es)"%(a[c], lista.count(a[c])))
    c += 1
