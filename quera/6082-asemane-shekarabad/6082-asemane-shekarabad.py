# https://quera.ir/problemset/contest/6082/سؤال-آسمان-شکر-آباد

inp = input().split(" ")
n, _ = int(inp[0]), int(inp[1])

counter = 0
for i in range(n):
    line = input()
    counter += line.count("*")

print(counter)
