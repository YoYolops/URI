""" TIME LIMIT EXCEEDED """

""" O Programa funciona! Mas não responde em tempo ágil, como aumentar a eficiência? """

while True:
    n = int(input())

    if n == 0:
        break

    loop = list(map(int, input().split()))  """ criando lista a partir dos inputs """
    listaSentido = []  """ lista para armazenar o sentido da onda, +1 para crescente -1 para decrescente """

    for i in range(len(loop)): """ por se tratar de um loop, o ultimo elemento da lista se relaciona ao primeiro
                                   assim, verifico se o elemento que estou analisando é o último """
        if i + 1 < len(loop):

            if loop[i] > loop[i + 1]: """ Sendo o valor seguinte menor, temos sentido decrescente, e adicionamos -1 """
                cente = -1            """ à lista auxiliar, caso contrário, adicionamos +1 """
                listaSentido.append(cente)
            else:
                cente = 1
                listaSentido.append(cente)
        else:                                 """ quando chego ao último elemento da lista, o comparo com o primeiro """
            if loop[(len(loop)-1)] > loop[0]:
                listaSentido.append(-1)
            else:
                listaSentido.append(1)

        inversao = 0                          """ estabeleço um contador para monitorar a quantidade de vezes que o sentido mudou """
        for i in range(len(listaSentido)):    """ pois quando o sentido muda, certamente há um pondo de inflexão """
            if i + 1 < len(listaSentido):
                if listaSentido[i] != listaSentido[i + 1]:  """ sempre cuidando para que o último elemento seja comparado com o primeiro """
                    inversao += 1
            else:
                if listaSentido[len(listaSentido)-1] != listaSentido[0]:
                    inversao += 1
    
    print(inversao) """ no fim, o valor armazenado em inversão é correspondente ao número de picos (máximos e mínimos) """
    
