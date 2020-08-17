""" TIME LIMIT EXCEEDED """

while True:
    n = int(input())

    if n == 0:
        break

    loop = list(map(int, input().split()))
    listaSentido = []

    for i in range(len(loop)):

        if i + 1 < len(loop):

            if loop[i] > loop[i + 1]:
                cente = -1
                listaSentido.append(cente)
            else:
                cente = 1
                listaSentido.append(cente)
        else:
            if loop[(len(loop)-1)] > loop[0]:
                listaSentido.append(-1)
            else:
                listaSentido.append(1)

        inversao = 0
        for i in range(len(listaSentido)):
            if i + 1 < len(listaSentido):
                if listaSentido[i] != listaSentido[i + 1]:
                    inversao += 1
            else:
                if listaSentido[len(listaSentido)-1] != listaSentido[0]:
                    inversao += 1
    
    print(inversao)
    
