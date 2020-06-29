comp, dped = input().split()
cukm, vaped = input().split()
comp = int(comp)
dped = int(dped)
cukm = int(cukm)
vaped = int(vaped)

valor = (int(comp/dped)*vaped)+cukm*comp
valor = int(valor)
print(valor)
