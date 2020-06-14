# https://quera.ir/problemset/contest/10327/سؤال-کدتخفیف

inp = input().split(" ")
n, t = int(inp[0]), inp[1]
result = []

for i in range(n):
    s = input()
    if set(s) == set(t):
        result.append("Yes")
    else:
        result.append("No")
print("\n".join(result))
