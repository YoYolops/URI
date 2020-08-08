# python3 "cédulas - 1018.py"

valor = int(input())

cem = int(valor/100)
valorMod = valor - cem * 100

cinquenta = int(valorMod/50)
valorMod = valorMod - cinquenta * 50

vinte = int(valorMod/20)
valorMod = valorMod - vinte * 20

dez = int(valorMod/10)
valorMod = valorMod - dez * 10

cinco = int(valorMod/5)
valorMod = valorMod - cinco * 5

dois = int(valorMod/2)
valorMod = valorMod - dois * 2

um = int(valorMod/1)


print(valor)
print("%d nota(s) de R$ 100,00" %cem)
print("%d nota(s) de R$ 50,00" %cinquenta)
print("%d nota(s) de R$ 20,00" %vinte)
print("%d nota(s) de R$ 10,00" %dez)
print("%d nota(s) de R$ 5,00" %cinco)
print("%d nota(s) de R$ 2,00" %dois)
print("%d nota(s) de R$ 1,00" %um)

