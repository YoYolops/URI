
h1, m1, h2, m2 = input().split()

h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

tempoSaida = (h1 * 60) + m1
tempoChegada = (h2 * 60) + m2

if tempoSaida >= tempoChegada:
    tempoSaida = (h1 * 60) + m1
    tempoChegada = (h2 * 60) + m2

    corrido = (24 * 60) - (tempoSaida - tempoChegada)
    duracaoH = int((corrido)/60)
    duracaoM = corrido % 60

    print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)'%(duracaoH, duracaoM))
else:
    duracaoH = int((tempoChegada - tempoSaida)/60)
    duracaoM = (tempoChegada - tempoSaida)%60

    print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)'%(duracaoH, duracaoM))