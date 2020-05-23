# https://quera.ir/problemset/contest/3414/سؤال-دو-نقطه-خط

inp = input().split(" ")
x1, y1, x2, y2 = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])

output = ""
if y1 == y2:
    output = "Horizontal"
elif x1 == x2:
    output = "Vertical"
else:
    output = "Try again"

print(output)
