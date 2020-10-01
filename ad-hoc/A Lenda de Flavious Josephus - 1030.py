
def matadora(lista, pulo):
    localMorte = pulo - 1
    manip = list(lista)
    mortos = []

    if pulo == 1:
        return manip[qPessoa - 1]
    else:
        while qPessoa != len(mortos) + 1:
            mortos.append(manip[localMorte])

            localMorte += pulo


            while localMorte >= len(manip):
                localMorte = (pulo - ((len(manip) - 1) - (localMorte - pulo)) - 1)

                for i in mortos:
                    if i in manip:
                        manip.pop(manip.index(i))
            


        return manip[0]

quantTeste = int(input())
times = 0
casoTeste = []

while quantTeste > 0:
    quantTeste -= 1

    qPessoa, salto = input().split()
    qPessoa = int(qPessoa)
    salto = int(salto)
    casoTeste.append([qPessoa, salto])

for i in casoTeste:
    qPessoa = i[0]
    salto = i[1]
    times += 1
    pessoas = []

    for j in range(1, i[0] + 1):
        pessoas.append(j)
    
    saida = matadora(pessoas, salto)

    print('Case %d: %d'%(times, saida))


    