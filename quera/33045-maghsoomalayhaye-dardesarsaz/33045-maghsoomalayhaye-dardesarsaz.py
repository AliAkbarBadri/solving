# https://quera.ir/problemset/contest/33045/سؤال-ریاضیات-مقسومعلیههای-دردسرساز

n = int(input())
all_numbers = []
all_numbers.append(1)
for i in range(2, n+1):
    all_numbers.append(1)
    for j in range(2, int(i/2)+1):
        if i % j == 0:
            all_numbers.append(j)
    all_numbers.append(i)
print(len(all_numbers), sum(all_numbers))
