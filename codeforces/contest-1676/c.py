# https://codeforces.com/contest/1676/problem/C

for _ in range(int(input())):
    minimum = 99999
    n ,m = input().split()
    words = []
    for _ in range(int(n)):
        words.append(input())
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            diff = sum([abs(ord(c1)-ord(c2)) for c1,c2 in zip(words[i],words[j])])
            if diff < minimum:
                minimum = diff
    print(minimum)