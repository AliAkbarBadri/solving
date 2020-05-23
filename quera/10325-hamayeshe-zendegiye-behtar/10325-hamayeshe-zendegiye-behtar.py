# https://quera.ir/problemset/contest/10325/سؤال-همایش-زندگی-بهتر

inp = input().split(" ")
row, column = int(inp[0]), int(inp[1])

direction = ""
down = 11 - row
walk = 0
if column > 10:
    direction = "Left"
    walk = 21 - column

else:
    direction = "Right"
    walk = column

print(direction, down, walk)
