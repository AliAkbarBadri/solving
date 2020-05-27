# https://quera.ir/problemset/contest/3540/سؤال-جست-و-جو-ریاضیات-گردو-شکستم

inp = input().split(" ")
n, x, y = int(inp[0]), int(inp[1]), int(inp[2])

length = n // x
width = (n % x) // y
output = -1
if length*x + width*y == n:
    output = str(length) + " " + str(width)
else:
    width = n // y
    length = (n % y) // x
    if length*x + width*y == n:
        output = str(length) + " " + str(width)
print(output)
