
while True:
    falha, caso = input().split()

    if falha == '0' and caso == '0':
        break

    caso = caso.replace(falha, '')

    if caso != '':
        caso = int(caso)
        print(caso)
    else:
        print(0)