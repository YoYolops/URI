# python3 "Teste de Seleção 1 - 1035.py"

a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)



testagem = [d > a, b > c, c + d > a + b, c > 0, d > 0, a % 2 == 0]

for i in testagem:
    if i == False:
        result = "Valores nao aceitos"
        break
    else:
        result = "Valores aceitos"
        
print(result)

