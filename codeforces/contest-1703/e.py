# https://codeforces.com/contest/1703/problem/D

for _ in range(int(input())):
    grid_size = int(input())
    a = [input() for _ in range(grid_size)]
    result = 0
    for i in range(grid_size):
        for j in range(grid_size):
            temp = int(a[i][j]) + int(a[j][~i]) + int(a[~i][~j]) + int(a[~j][i])
            result += min(temp, 4-temp)
    print(int(result/4))