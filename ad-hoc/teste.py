
"""  """
n = int(input())
regioes = []

for i in range(n):
    c = i + 1
    regioes.append(c)



opcao = list(regioes)
saltosPossiveis = []
passo = 0
m = 5
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

    print(saltosPossiveis)

"""     print('passo final: %d'%passo) """


 

""" while True:
    n = int(input())
    regioes = []

    if n == 0:
        break
    
    for i in range(n):
        c = i + 1
        regioes.append(c)

    print(regioes) """







