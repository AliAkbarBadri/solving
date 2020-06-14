# https://quera.ir/problemset/contest/2794/سؤال-دوربین-مداربسته

inp = input().split(" ")
x1, y1 = int(inp[0]), int(inp[1])
inp = input().split(" ")
x2, y2 = int(inp[0]), int(inp[1])
inp = input().split(" ")
x3, y3 = int(inp[0]), int(inp[1])
x4, y4 = -1, -1

if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1

if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1

print(x4, y4)
