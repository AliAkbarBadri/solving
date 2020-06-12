# https://quera.ir/problemset/contest/10231/سؤال-خب-باقر-سرما-خورده

n = 5
words = []
for i in range(n):
    word = input()
    if "HAFEZ" in word or "MOLANA" in word:
        words.append(str(i+1))
if len(words) != 0:
    print(" ".join(words))
else:
    print("NOT FOUND!")
