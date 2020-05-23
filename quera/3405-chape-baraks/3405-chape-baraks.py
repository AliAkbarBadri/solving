# https://quera.ir/problemset/contest/3405/سؤال-چاپ-برعکس
inp = 1
numbers = []
while inp != 0:
    inp = int(input())
    numbers.append(inp)

for i in range(len(numbers)-2, -1, -1):
    print(numbers[i])
