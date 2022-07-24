# https://codeforces.com/contest/1352/problem/A

for _ in range(int(input())):
    a = input()
    numbers = []
    count = 1
    for i in range(len(a)):
        if int(a[i]):
            numbers.append(a[i] + (len(a) - i - 1) * "0")
    print(len(numbers))
    print(*numbers, sep=" ")
