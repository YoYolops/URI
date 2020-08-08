h, m = input().split()
h = int(h)
m = int(m)

hora = int(h/30)
minuto = int(m/6)

if hora >= 10 and minuto >= 10:
    print("%d:%d"%(hora, minuto))
elif hora >= 10 and minuto < 10:
    print("%d:0%d"%(hora, minuto))
elif hora < 10 and minuto < 10:
    print("0%d:0%d"%(hora, minuto))
elif hora < 10 and minuto >= 10:
    print("0%d:%d"%(hora, minuto))
