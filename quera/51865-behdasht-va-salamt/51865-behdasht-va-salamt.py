# https://quera.ir/problemset/contest/51865/سؤال-پیاده-سازی-بهداشت-و-سلامت

grade = int(input())
days = int(input())
output = 0

if days == 0:
    output = 20
elif days == 7:
    output = grade
else:
    output = max([grade - days, 0])
print(output)
