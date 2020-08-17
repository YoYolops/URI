# 5% errado

day = int(input())
mes = int(day/30)
ano = int(mes/12)

if day < 30:
    print("0 ano(s)")
    print("0 mes(es)")
    print("%d dia(s)"%day)
elif 365 > day >= 30:
    day = day - mes*30
    print("0 ano(s)")
    print("%d mes(es)"%mes)
    print("%d dia(s)"%day)
elif day >= 365:
    day = day - mes*30
    mes = mes - ano*12
    print("%d ano(s)"%ano)
    print("%d mes(es)"%mes)
    print("%d dia(s)"%day)
