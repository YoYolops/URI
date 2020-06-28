# Runtime Error dentro do while

a = int(input())
n = 1
for i in range(a):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    popa = pa + int(pa * g1)
    popb = pb + int(pb * g2)
    while popa != popb:
        popa += int(popa * g1)
        popb += int(popb * g2)
        n += n
        print("%d anos"%n)


# JUST CODING (FROM BRASIL!)
# PYTHON 3
# QUESTIONS FROM https://www.urionlinejudge.com.br
