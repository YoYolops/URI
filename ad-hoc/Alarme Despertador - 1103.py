
while True:
    h1, m1, h2, m2 = input().split()
    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int (m2)
    minutosDia = []
    stop = [h1 == 0, m1 == 0, h2 == 0, m2 == 0]

    for i in stop:
        if i == False:
            stop = False
            break
        else:
            stop = True

    if stop == True:
        break

    entradaUm = (h1 * 60) + m1
    entradaDois = (h2 * 60) + m2

    if entradaUm < entradaDois:
        result = entradaDois - entradaUm
    else:
        result = (1440 - entradaUm) + entradaDois

    print(result)




