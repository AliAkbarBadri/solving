# https://quera.ir/problemset/contest/10326/سؤال-استارت-آپ-باکلاس

inp = [int(i) for i in input().split(" ")]
output = [0, 0, 0, 0]
i = 0
while not 0 in inp:
    inp[i] -= 1
    output[i] += 1
    inp.append(inp.pop(0))
    i += 1
    if i == len(inp):
        i = 0

print(" ".join(str(x) for x in output))
