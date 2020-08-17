cod1, quant1, valor1 = input().split()
quant1 = int(quant1)
valor1 = float(valor1)

cod2, quant2, valor2 = input().split()
quant2 = int(quant2)
valor2 = float(valor2)

valort = (quant1 * valor1) + (quant2 * valor2)
print("VALOR A PAGAR: R$ %.2f"%valort)
