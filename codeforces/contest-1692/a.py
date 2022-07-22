# https://codeforces.com/contest/1692/problem/A

for _ in range(int(input())):
    a = list(map(int, input().split()))
    result = 0
    for i in a[1:]:
        if i > a[0]:
            result += 1
    print(result)