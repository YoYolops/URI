
indnum = ['1', '2', '3', '4', '5', '6', '7', '8']
indlet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

listaDeListas = []
pospecas = []
pecas = NAN


def puloCavalo(cal):
    casascavalo = []
    if cal[0] not in ['7','8']:
        cima = [ indnum[indnum.index(cal[0]) + 2] + indlet[indlet.index(cal[1]) + 1], indnum[indnum.index(cal[0]) + 2] + indlet[indlet.index(cal[1]) - 1] ]
        if cal[1] != 'h':
            casascavalo.append(cima[0])
        if cal[1] != 'a':
            casascavalo.append(cima[1])

    if cal[0] not in ['1','2']:
        baixo = [ indnum[indnum.index(cal[0]) - 2] + indlet[indlet.index(cal[1]) + 1], indnum[indnum.index(cal[0]) - 2] + indlet[indlet.index(cal[1]) - 1] ]
        if cal[1] != 'h':
            casascavalo.append(baixo[0])
        if cal[1] != 'a':
            casascavalo.append(baixo[1])

    if cal[1] not in ['g','h']:
        direita = [ indnum[indnum.index(cal[0]) + 1] + indlet[indlet.index(cal[1]) + 2], indnum[indnum.index(cal[0]) - 1] + indlet[indlet.index(cal[1]) + 2] ]
        if cal[0] != '8':
            casascavalo.append(direita[0])
        if cal[0] != '1':
            casascavalo.append(direita[1])

    if cal[1] not in ['a','b']:
        esquerda = [ indnum[indnum.index(cal[0]) + 1] + indlet[indlet.index(cal[1]) - 2], indnum[indnum.index(cal[0]) - 1] + indlet[indlet.index(cal[1]) - 2] ]
        if cal[0] != '8':
            casascavalo.append(esquerda[0])
        if cal[0] != 1:
            casascavalo.append(esquerda[1])
        
    return casascavalo

def dominioPeao(peao):
    casasdominadas = []

    for i in peao:

        if i[1] != '1':
            if i[1] != 'a':
                esquerda = indnum[indnum.index(i[0]) - 1] + indlet[indlet.index(i[1]) - 1]
                casasdominadas.append(esquerda)
            if i[1] != 'h':
                direita = indnum[indnum.index(i[0]) - 1] + indlet[indlet.index(i[1]) + 1]
                casasdominadas.append(direita)

    return casasdominadas
        
def solucao(caso):
    a = puloCavalo(cavalo)
    b = dominioPeao(caso)
    cont = 0

    for i in a:
        if i in b:
            cont += 1

    resposta = len(a) - cont
    print('Caso de Teste #%d: %d movimento(s).'%(,resposta))


while True:
    pecas = input()

    if pecas == '0':
        break

    pospecas.append(pecas)

    if len(pospecas) == 8:
        listaDeListas.append(pospecas)
        pospecas = []

    else:
        cavalo = pospecas[0]
        pospecas.pop(0)
        solucao()

for i in len(listaDeListas):
    
    cavalo = listaDeListas[i][0]
    listaDeListas[i].pop(0)
    solucao(i)


        


    