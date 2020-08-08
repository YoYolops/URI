# python3 "Idade em Dias - 1020.py"

valor = int(input())

ano = int(valor/365)
valorMod = valor - ano * 365

mes = int(valorMod/30)
valorMod = valorMod - mes * 30

dia = valorMod



print("%d ano(s)" %ano)
print("%d mes(es)" %mes)
print("%d dia(s)" %dia)

