
indnum = ['1', '2', '3', '4', '5', '6', '7', '8']
indlet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

pospecas = []

def puloCavalo(cal):

    cima = [ indnum[indnum.index(cal[0]) + 2] + indlet[indlet.index(cal[1]) + 1], indnum[indnum.index(cal[0]) + 2] + indlet[indlet.index(cal[1]) - 1] ]

    baixo = [ indnum[indnum.index(cal[0]) - 2] + indlet[indlet.index(cal[1]) + 1], indnum[indnum.index(cal[0]) - 2] + indlet[indlet.index(cal[1]) - 1] ]

    direita = [ indnum[indnum.index(cal[0]) + 1] + indlet[indlet.index(cal[1]) + 2], indnum[indnum.index(cal[0]) - 1] + indlet[indlet.index(cal[1]) + 2] ]

    esquerda = [ indnum[indnum.index(cal[0]) + 1] + indlet[indlet.index(cal[1]) - 2], indnum[indnum.index(cal[0]) - 1] + indlet[indlet.index(cal[1]) - 2] ]
    
    casascavalo = [cima[0], cima[1], baixo[0], baixo[1], direita[0], direita[1], esquerda[0], esquerda[1]]


def dominioPeao(peao):
    casasdominadas = []

    for i in peao:
        esquerda = [ indnum[i[0] - 1] + indlet[i[1] - 1] ]
        direita = [ indnum[i[0] - 1] + indlet[i[1] + 1] ]

        


while True:

    pecas = str(input())

    if pecas != '0':
        pospecas.append(pecas)

    else:
        cavalo = pospecas[0]    
        pospecas.pop(0)

        puloCavalo(cavalo)


        


    