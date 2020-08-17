x1 = int(input())
x2 = int(input())
x3 = int(input())

top = int(x2 * 2 + (x3 * 4))
mid = int(x1 * 2 + (x3 * 2))
bot = int(x1 * 4 + (x2 * 2))

print(min(top, mid, bot))
