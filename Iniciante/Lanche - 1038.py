"""python3 "Lanche - 1038.py" """

cod, quant = split().input()

precos = {
    'id': 1,
    'preco': 4,
    '2': 4.5,
    '3': 5,
    '4': 2,
    '5': 1,5
    }

cod = str(int(cod))
quant = int(quant)

for i in precos:
    if cod == i:
        valor = cod.value * quant
        break

print("Total: R$ %.2f"%valor)