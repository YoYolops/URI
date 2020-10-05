
c = 0
val = []
while c < 6:
    a = float(input())
    val.append(a)
    c +=1

cont = 0

for i in val:
    if i > 0:
        cont += 1

print('%d valores positivos'%cont)