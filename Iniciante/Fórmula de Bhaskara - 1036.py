a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

delta = (pow(b, 2)) - (4*a*c)

if delta < 0 or 2*a == 0:
    print('Impossivel calcular')
    exit()

raiz1 = (-1*b + pow(delta, 1/2))/(2*a)
raiz2 = (-1*b - pow(delta, 1/2))/(2*a)

print('R1 = %.5f'%raiz1)
print('R2 = %.5f'%raiz2)
