while True:
  try:
    e = int(input())
    n = list(map(int, input().split()))
    if max(n, key=int) < 10:
        print(1)
    elif 10 <= max(n, key=int) < 20:
        print(2)
    elif 20 <= max(n, key=int):
        print(3)
  except EOFError:
    break
