
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

        casasdominadas = []

#        for i in pospecas:
#            esquerda = [ indnum[indnum.index(i[0]) - 1] + indlet[indlet.index(i[1]) - 1] ]
#            direita = [ indnum[indnum.index(i[0]) - 1] + indlet[indlet.index(i[1]) + 1] ]
#            casasdominadas.append(esquerda)
#            casasdominadas.append(direita)
#        print(casasdominadas)

        cima = [ indnum[indnum.index(cavalo[0]) + 2] + indlet[indlet.index(cavalo[1]) + 1], indnum[indnum.index(cavalo[0]) + 2] + indlet[indlet.index(cavalo[1]) - 1] ]

        baixo = [ indnum[indnum.index(cavalo[0]) - 2] + indlet[indlet.index(cavalo[1]) + 1], indnum[indnum.index(cavalo[0]) - 2] + indlet[indlet.index(cavalo[1]) - 1] ]

        direita = [ indnum[indnum.index(cavalo[0]) + 1] + indlet[indlet.index(cavalo[1]) + 2], indnum[indnum.index(cavalo[0]) - 1] + indlet[indlet.index(cavalo[1]) + 2] ]

        esquerda = [ indnum[indnum.index(cavalo[0]) + 1] + indlet[indlet.index(cavalo[1]) - 2], indnum[indnum.index(cavalo[0]) - 1] + indlet[indlet.index(cavalo[1]) - 2] ]

        print(cima)
        casascavalo = [cima[0], cima[1], baixo[0], baixo[1], direita[0], direita[1], esquerda[0], esquerda[1]]
        print(casascavalo)


        while True:

    pecas = input()

    if pecas != '0':
        pospecas.append(pecas)

    else:
        cavalo = pospecas[0]    
        pospecas.pop(0)
    
        solucao()

for i in range(5):
    print(i)

