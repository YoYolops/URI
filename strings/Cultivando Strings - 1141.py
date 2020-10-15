
while True:
    registro = []
    caso = int(input())

    if caso == 0:
        break

    while caso > 0:
        caso -= 1

        registro.append(input())

    manipulacao = list(registro)
    regPalMudada = []

    for i in registro:
        palMudada = 0

        for j in manipulacao:
            preLen = len(j)
            j = j.replace(i, '')
            posLen = len(j)

            if preLen > posLen:
                palMudada += 1
        
        manipulacao = list(registro)
        regPalMudada.append(palMudada)
        print(regPalMudada)

    c = 0
    for k in regPalMudada:
        if k > c:
            c = k
    
    print(c)
