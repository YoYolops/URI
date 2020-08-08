# python3 "Gasto de Combustível - 1017.py"

tempoGasto = int(input())
velocidadeMedia = int(input())

litrosPrecisos = (velocidadeMedia * tempoGasto)/12

print('%.3f' %litrosPrecisos)