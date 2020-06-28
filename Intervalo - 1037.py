a = float(input())

if 0 <= a <= 25.00:
    print("Intervalo [0,25]")
elif 25.00 < a <= 50.00:
    print("Intervalo (25,50]")
elif 50.00 < a <= 75.00:
    print("Intervalo (50,75]")
elif 75.00 < a <= 100.00:
    print("Intervalo (75,100]")
elif a > 100 or a < 0:
    print("Fora de intervalo")
