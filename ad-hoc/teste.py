
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

qPessoa, salto = input().split()
qPessoa = int(qPessoa)
salto = int(salto)
pessoas = []

for i in range(1, qPessoa + 1):
    pessoas.append(i)

saida = matadora(pessoas, salto)

print(saida)




        

        
