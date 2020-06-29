while True:
  try:
    hora = input()
    h = hora[0]
    min = hora[2:4]
    h = int(h)
    min = int(min)

    if h >= 8:
        atrasoh = 60 + (h - 8)*60 + min
        print("Atraso maximo: %d"%atrasoh)
    elif 7 == h:
        print("Atraso maximo: %d"%min)
    else:
        print("Atraso maximo: 0")
  except EOFError:
    break
