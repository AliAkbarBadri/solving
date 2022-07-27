# https://codeforces.com/contest/1352/problem/C

for _ in range(int(input())):
    inp = input().split()
    n ,k = int(inp[0]), int(inp[1])
    print(k + (k-1)//(n-1))