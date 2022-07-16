# https://codeforces.com/contest/1703/problem/B
n = int(input())

for i in range(n):
    _ = int(input())
    balloons = 0
    balloons_set = set()
    questions = input()
    for char in questions:
        if char in balloons_set:
            balloons += 1
        else:
            balloons += 2
            balloons_set.add(char)
    print(balloons)