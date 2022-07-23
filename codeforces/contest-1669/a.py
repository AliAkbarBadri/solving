# https://codeforces.com/contest/1669/problem/A

for _ in range(int(input())):
    number = int(input())
    if number <= 1399:
        print("Division 4")
    elif 1400 <= number and number <= 1599:
        print("Division 3")
    elif  1600<= number and number <= 1899:
        print("Division 2")
    elif 1900 <= number:
        print("Division 1")