seg = int(input())
min = int(seg/60)
h = int(min/60)

if seg < 60:
    print("0:0:%i"%seg)
elif seg in range(60, 3600):
    seg = seg - (min * 60)
    print("0:%d:%d"%(min, seg))
elif seg >= 3600:
    seg = seg - (min * 60)
    min = min - (h * 60)
    print("%d:%d:%d"%(h, min, seg))

# Código de Leo(leleoveiga):

x = int(input())

horas = int(x/3600)
x -= horas*3600
minutos = int(x/60)
x -= minutos*60
segundos = int(x)

print(str(horas) + ":" + str(minutos) + ":" + str(segundos))
