# https://quera.ir/problemset/contest/2529/سؤال-اسمها

n = int(input())
result = -1
for i in range(n):
    name = input()
    temp = len(set(name))
    if temp > result:
        result = temp
print(result)
