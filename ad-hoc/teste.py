
indnum = ['1', '2', '3', '4', '5', '6', '7', '8']
indlet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

pospecas = []
listaDeListas = []

while True:
    pecas = input()

    if pecas == '0':
        break

    pospecas.append(pecas)

    if len(pospecas) == 8:
        listaDeListas.append(pospecas)
        pospecas = []

    print(listaDeListas)
    


