indnum = ['1', '2', '3', '4', '5', '6', '7', '8']
indlet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

listaDeListas = []
pospecas = []
contadorGeral = 0

def puloCavalo(cal):
    casascavalo = []
    if cal[0] not in ['7','8']:
        if cal[1] != 'h':
            cimaRight = indnum[indnum.index(cal[0]) + 2] + indlet[indlet.index(cal[1]) + 1]
            casascavalo.append(cimaRight)
        if cal[1] != 'a':
            cimaLeft = indnum[indnum.index(cal[0]) + 2] + indlet[indlet.index(cal[1]) - 1]
            casascavalo.append(cimaLeft)

    if cal[0] not in ['1','2']:
        baixo = indnum[indnum.index(cal[0]) - 2] + indlet[indlet.index(cal[1]) - 1]
        if cal[1] != 'h':
            baixoRight = indnum[indnum.index(cal[0]) - 2] + indlet[indlet.index(cal[1]) + 1]
            casascavalo.append(baixoRight)
        if cal[1] != 'a':
            baixoLeft = indnum[indnum.index(cal[0]) - 2] + indlet[indlet.index(cal[1]) - 1]
            casascavalo.append(baixoLeft)

    if cal[1] not in ['g','h']:
        if cal[0] != '8':
            direitaUp = indnum[indnum.index(cal[0]) + 1] + indlet[indlet.index(cal[1]) + 2]
            casascavalo.append(direitaUp)
        if cal[0] != '1':
            direitaDown = indnum[indnum.index(cal[0]) - 1] + indlet[indlet.index(cal[1]) + 2]
            casascavalo.append(direitaDown)

    if cal[1] not in ['a','b']:
        esquerda = indnum[indnum.index(cal[0]) - 1] + indlet[indlet.index(cal[1]) - 2]
        if cal[0] != '8':
            esquerdaUp = indnum[indnum.index(cal[0]) + 1] + indlet[indlet.index(cal[1]) - 2]
            casascavalo.append(esquerdaUp)
        if cal[0] != 1:
            esquerdaDown = indnum[indnum.index(cal[0]) - 1] + indlet[indlet.index(cal[1]) - 2]
            casascavalo.append(esquerdaDown)
        
    return casascavalo

def dominioPeao(peao):
    casasdominadas = []

    for j in peao:

        if j[1] != '1':
            if j[1] != 'a':
                esquerda = indnum[indnum.index(j[0]) - 1] + indlet[indlet.index(j[1]) - 1]
                casasdominadas.append(esquerda)
            if j[1] != 'h':
                direita = indnum[indnum.index(j[0]) - 1] + indlet[indlet.index(j[1]) + 1]
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
    print('Caso de Teste #%d: %d movimento(s).'%(contadorGeral, resposta))


while True:
    pecas = input()

    if pecas == '0':
        break

    pospecas.append(pecas)

    if len(pospecas) == 9:
        listaDeListas.append(pospecas)
        pospecas = []


for i in range(len(listaDeListas)):
    contadorGeral += 1

    cavalo = listaDeListas[i][0]
    listaDeListas[i].pop(0)
    solucao(listaDeListas[i])


        


    