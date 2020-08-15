""" python3 "Crise de Energia - 1031.py" """

""" OBS: Esse programa não para enquanto não encontra uma solução. Talvez seja prudente adicionar um if que pare o loop quando
o "m" passar do valor de input, pois passando desse valor, certamente não existe solução """

def organiza(lista, salto):
    opcao = list(regioes)
    saltosPossiveis = []
    passo = 0
    m = salto
    escolhidos = []

    while len(regioes) != len(saltosPossiveis):

        if opcao[passo] not in saltosPossiveis:
            saltosPossiveis.append(opcao[passo])
            escolhidos.append(opcao[passo])
            passo += m

        if passo >= len(opcao):

            for i in escolhidos:
                opcao.pop(opcao.index(i))
                excluidos = len(escolhidos)

            escolhidos = []
            passo -= excluidos

            while passo >= len(opcao):
                passo = passo - (len(opcao))
                if len(opcao) == 0:
                    break

    l = len(saltosPossiveis)

    if saltosPossiveis[l - 1] != 13:
        salto += 1
        organiza(regioes, salto)
    else:
        print(m)



while True:
    n = int(input())
    regioes = []

    if n == 0:
        break
    
    for i in range(n):
        c = i + 1
        regioes.append(c)

    organiza(regioes, 1)



