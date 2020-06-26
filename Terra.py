while True:
  try:
    grau = int(input())

    if(grau in range(0, 90) or grau == 360):
        print("Bom Dia!!")
    elif(grau in range(90, 180)):
        print("Boa Tarde!!")
    elif(grau in range(180, 270)):
        print("Boa Noite!!")
    elif(grau in range(270, 360)):
        print("De Madrugada!!")
  except EOFError:
    break
