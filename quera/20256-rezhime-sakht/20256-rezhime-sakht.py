# https://quera.ir/problemset/contest/20256/سؤال-رژیم-سخت

inp = input()

output = "rahat baash"
if (inp.count('R') >= 3) or (inp.count('R') >= 2 and inp.count('Y') >= 2) or ("G" not in inp):
    output = "nakhor lite"

print(output)
