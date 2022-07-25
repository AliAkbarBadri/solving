# https://codeforces.com/contest/1676/problem/B

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    min_number = 10**8
    sum = 0
    for item in a:
        sum += item
        if item < min_number:
            min_number = item
    print(sum - n*min_number)