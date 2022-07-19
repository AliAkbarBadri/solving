# https://codeforces.com/contest/1703/problem/G
import math
n_test_cases = int(input())
 
def solve(a, idx, k):
    if idx == len(a)-1:
        return max(a[idx]-k,  math.floor(idx/2))
    else:
        return max(solve(a, idx+1, k))
    return
for i in range(n_test_cases):
    n_chests , k = list(map(int, input().split(" ")))
    chests = list(map(int, input().split()))
    results = 0
    solve(chests, 9, k)
    