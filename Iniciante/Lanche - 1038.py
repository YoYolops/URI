
produtos = {
    '1':4.00,
    '2':4.50,
    '3':5.00,
    '4':2.00,
    '5':1.50
}

codigo, quant = input().split()
codigo = codigo
quant = int(quant)

total = (produtos[codigo]) * quant

print('Total: R$ %.2f'%total)