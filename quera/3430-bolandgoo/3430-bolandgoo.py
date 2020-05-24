# https://quera.ir/problemset/contest/3430/سؤال-بلندگو

inp = input()

for i in range(len(inp)):
    inp = i*inp[i]+inp[i:]
    print(inp)
