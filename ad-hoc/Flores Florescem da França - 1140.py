
while True:
    frase = input().split()
    lowCase = []

    if frase == ['*']:
        break

    for i in frase:
       lowCase.append(i.lower())
    
    primeira = lowCase[0]
    for i in lowCase:
        if i[0] == primeira[0]:
            result = 'Y'
        else:
            result = 'N' 
            break
    print(result)       

