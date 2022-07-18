# https://codeforces.com/contest/1703/problem/F
n_test_cases = int(input())
 
for i in range(n_test_cases):
    n_array = int(input())
    a = [0] + [int(item) for item in input().split(" ")]
    results = 0
    answer = [0]*(n+1)
    for i in range(n_array, 0, -1):
        if a[i] < i:
            for j in range(a[i]-1, 0, -1):
                if a[j] < j:
                    results += 1
    print(results)