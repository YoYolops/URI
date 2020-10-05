
cartasA = []
cartasB = []

while True:
    quantA, quantB = input().split()
    if quantA == '0' or quantB == '0':
        break

    cartasA = input().split()
    cartasB = input().split()

    enviaA = 0
    lastro = 'vazio'
    for i in cartasA:
        if i == lastro:
            continue
        
        lastro = i
        if i not in cartasB:
            enviaA += 1

    enviaB = 0
    lastro = 'vazio'
    for i in cartasB:
        if i == lastro:
            continue

        lastro = i
        if i not in cartasA:
            enviaB += 1
        
    if enviaA >= enviaB:
        print(enviaB)
    else:
        print(enviaA)


#################################################################


cartasA = []
cartasB = []
respostas = []

while True:
    quantA, quantB = input().split()
    
    if quantA == '0' or quantB == '0':
        for i in respostas:
            print(i)
        break

    cartasA = input().split()
    cartasB = input().split()

    enviaA = 0
    lastro = 'vazio'
    for i in cartasA:
        if i == lastro:
            continue
        
        lastro = i
        if i not in cartasB:
            enviaA += 1

    enviaB = 0
    lastro = 'vazio'
    for i in cartasB:
        if i == lastro:
            continue

        lastro = i
        if i not in cartasA:
            enviaB += 1
        
    if enviaA >= enviaB:
        respostas.append(enviaB)
    else:
        respostas.append(enviaA)