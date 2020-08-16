while True:
    frase = input().split()
    lowCase = []

    for i in frase:
       lowCase.append(i.lower())
        

    print(lowCase)

    if frase == ['*']:
        break