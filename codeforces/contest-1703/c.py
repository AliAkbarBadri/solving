# https://codeforces.com/contest/1703/problem/C
n_test_cases = int(input())

for i in range(n_test_cases):
    n_wheels = int(input())
    final_wheels = input().split(' ')
    for i in range(n_wheels):
        wheel_actions = input().split(' ')[1]
        final_action = 0
        for wheel_action in wheel_actions:
            if wheel_action == 'D':
                final_action += 1
            else:
                final_action -= 1
        final_wheels[i] = (int(final_wheels[i]) + final_action) % 10
    print(*final_wheels, sep=' ')