a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

conjunto = [a,b,c]
conjunto = sorted(conjunto)

istri = [
    conjunto[2] - conjunto[1] < conjunto[0] < conjunto[2] + conjunto[1],
    conjunto[2] - conjunto[0] < conjunto[1] < conjunto[2] + conjunto[0],
    conjunto[1] - conjunto[0] < conjunto[2] < conjunto[1] + conjunto[0]
]

if False not in istri:
    soma = 0

    for i in conjunto:
        soma += i

    print('Perimetro = %.1f'%soma)

else:
    area = ((a + b) * c)/2

    print('Area = %.1f'%area)