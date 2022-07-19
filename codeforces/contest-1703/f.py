# https://codeforces.com/contest/1703/problem/F
n_test_cases = int(input())
 
for i in range(n_test_cases):
    n_array = int(input())
    a = [0] + [int(item) for item in input().split(" ")]
    results = 0
    answers = [0]*(n_array+1)
    for i in range(1, n_array+1):
        answers[i] = answers[i-1]+ (a[i]<i)
        if a[i] < i:
            results += answers[max(0,a[i]-1)]
    print(results)