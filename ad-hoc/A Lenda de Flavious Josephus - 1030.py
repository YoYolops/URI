
quantTeste = int(input())
times = 0

def matadora(lista, salto):
    localMorte = salto - 1
    manip = list(lista)
    mortos = []
    
    while qPessoa != len(mortos) + 1:
        mortos.append(lista[localMorte])

        localMorte += 2

        if localMorte >= len(lista):
            localMorte -= (len(manip) - len(mortos)) + 2

            for i in mortos:
                manip.pop(manip.index(i))
    
    return manip[0]

while quantTeste != 0:
    times += 1
    quantTeste -= 1

    qPessoa, salto = input().split()
    qPessoa = int(qPessoa)
    salto = int(salto)
    pessoas = []

    for i in range(1, qPessoa + 1):
        pessoas.append(i)

    saida = matadora(pessoas, salto)

    print('Case %d: %d'%(times, saida))

    