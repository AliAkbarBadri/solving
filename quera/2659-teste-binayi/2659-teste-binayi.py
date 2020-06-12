# https://quera.ir/problemset/contest/2659/سؤال-تست-بینایی

_ = int(input())
str1 = input()
str2 = input()
counter = 0
for i in range(len(str1)):
    if str1[i] != str2[i]:
        counter += 1
print(counter)
