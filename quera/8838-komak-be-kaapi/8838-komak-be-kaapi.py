# https://quera.ir/problemset/contest/8838/سؤال-کمک-به-کاپی

inp = input().split(" ")
n, s = int(inp[0]), inp[1]
output = "".join(["copy of " for i in range(n)]) + s
print(output)
