# https://quera.ir/problemset/contest/31025/سؤال-پیاده-سازی-صبا-و-سوال-ساده

inp = input().split(" ")
n, k = int(inp[0]), int(inp[1])
result = n // (2**k)
print(result)
