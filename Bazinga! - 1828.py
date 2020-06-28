# 10% Errada

e = int(input())
caso = 1

for i in range(e):
    f = list(map(str, input().split()))
    if f[0] == "pedra":
        if f[1] == "tesoura" or f[1] == "lagarto":
            print("Caso #%d: Bazinga!"%caso)
        else:
            print("Caso #%d: Raj trapaceou!"%caso)

    elif f[0] == "papel":
        if f[1] == "pedra" or f[1] == "Spock":
            print("Caso #%d: Bazinga!"%caso)
        else:
            print("Caso #%d: Raj trapaceou!"%caso)

    elif f[0] == "tesoura":
        if f[1] == "papel" or f[1] == "lagarto":
            print("Casp #%d: Bazinga!"%caso)
        else:
            print("Caso #%d: Raj trapaceou!"%caso)

    elif f[0] == "lagarto":
        if f[1] == "Spock" or f[1] == "papel":
            print("Caso #%d: Bazinga!"%caso)
        else:
            print("Caso #%d: Raj trapaceou!"%caso)

    elif f[0] == "Spock":
        if f[1] == "tesoura" or f[1] == "pedra":
            print("Caso #%d: Bazinga!"%caso)
        else:
            print("Caso #%d: Raj trapaceou!"%caso)

    elif f[0] == f[1]:
        print("Caso #%d: De novo!"%caso)
    caso = caso + 1
