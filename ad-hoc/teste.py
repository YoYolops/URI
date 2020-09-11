
indnum = ['1', '2', '3', '4', '5', '6', '7', '8']
indlet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

pospecas = []

while True:

    pecas = str(input())

    if pecas != '0':
        pospecas.append(pecas)

    else:
        cavalo = pospecas[0]    
        pospecas.pop(0)

        cima = [ indnum[indnum.index(cavalo[0]) + 2] + indlet[indlet.index(cavalo[1]) + 1], indnum[indnum.index(cavalo[0]) + 2] + indlet[indlet.index(cavalo[1]) - 1] ]

        print(pospecas)


