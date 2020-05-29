# https://quera.ir/problemset/contest/2705/سؤال-بدخواه-پویان

inp = input().split(" ")
p, d = int(inp[0]), int(inp[1])

output = 0
mod = p

while mod > p/2:
    output += d
    mod = output % p

print(output)
