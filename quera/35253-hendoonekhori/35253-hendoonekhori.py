# https://quera.ir/problemset/contest/35253/سؤال-پیاده-سازی-هندونهخوری

_ = input()
inp = input().strip().split(" ")
numbers = [int(x) for x in inp]
print(numbers.index(max(numbers))+1)
