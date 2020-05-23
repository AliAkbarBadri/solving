# https://quera.ir/problemset/contest/3409/سؤال-جدول-ضرب-گنده

n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i*j, end=' ')
    print("\n")
