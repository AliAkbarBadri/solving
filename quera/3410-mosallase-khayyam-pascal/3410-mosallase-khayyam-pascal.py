# https://quera.ir/problemset/contest/3410/سؤال-پیاده-سازی-ریاضیات-مثلث-خیام-پاسکال

n = int(input())
triangle = []

for i in range(n):
    triangle.append([])
    for j in range(i+1):
        if j == i or j == 0:
            triangle[i].append(1)
        else:
            triangle[i].append(triangle[i-1][j] + triangle[i-1][j-1])
    print(" ".join([str(x) for x in triangle[i]]))
