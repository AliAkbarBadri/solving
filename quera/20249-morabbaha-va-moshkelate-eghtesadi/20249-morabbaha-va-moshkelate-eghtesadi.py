# https://quera.ir/problemset/contest/20249/سؤال-مرباها-و-مشکلات-اقتصادی

inp = input().split(" ")
n, k = int(inp[0]), int(inp[1])
inp = input().split(" ")
sum = 0
for x in inp:
    sum += int(x)
print(max([n - round(sum/k), 0]))
