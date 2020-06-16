# https://quera.ir/problemset/contest/49535/سؤال-پیاده-سازی-گزارش-کار

inp = input().split(" ")
n, k = int(inp[0]), int(inp[1])
sum = 0
for i in range(n):
    sum += int(input())
if sum >= k:
    print("YES")
else:
    print("NO")
