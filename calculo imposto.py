renda = float(input())

if(renda <= 2000.00):
    print("Isento")
elif(renda > 2000.00 and renda <= 3000.00):
    valor = 0.08 * (renda - 2000.00)
    print("R$ %.2f"%valor)
elif(renda > 3000.00 and renda <= 4500.00):
    valor = (0.18 * (renda - 3000.00)) + (0.08 * 1000.00)
    print("R$ %.2f"%valor)
elif(renda > 4500.00):
    valor = (0.28 * (renda - 4500.00)) + (0.18 * 1500.00) + (0.08 * 1000.00)
    print("R$ %.2f"%valor)
