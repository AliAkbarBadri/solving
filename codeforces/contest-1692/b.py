# https://codeforces.com/contest/1692/problem/B

for _ in range(int(input())):
    n = int(input())
    numbers = dict()    
    a = list(map(int, input().split()))
    distincts = set(a)
    if (n - len(distincts)) % 2:
        print(len(distincts) - 1)
    else:
        print(len(distincts))