x, y = input().split()
x = float(x)
y = float(y)

if x == 0 and y == 0:
    print('Origem')

elif x == 0 and y !=0:
    print('Eixo Y')

elif x > 0:
    if y > 0:
        print('Q1')
    elif y < 0:
        print('Q4')
    else:
        print('Eixo X')

else:
    if y > 0:
        print('Q2')
    elif y < 0:
        print('Q3')
    else:
        print('Eixo X')