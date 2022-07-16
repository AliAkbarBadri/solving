# https://codeforces.com/contest/1703/problem/A
n = int(input())

for i in range(n):
    inp = input()
    print("YES") if inp.lower() == "yes" else print("NO")