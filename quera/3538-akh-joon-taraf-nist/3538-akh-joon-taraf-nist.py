# https://quera.ir/problemset/contest/3538/سؤال-آخ-جون-طرف-نیست

number = 3
days = set(["shanbe", "1shanbe", "2shanbe",
            "3shanbe", "4shanbe", "5shanbe", "jome"])
days_on = set()
for i in range(number):
    k = int(input())
    friend_days = input().split(" ")
    for friend_day in friend_days:
        days_on.add(friend_day)

print(len(days.difference(days_on)))
