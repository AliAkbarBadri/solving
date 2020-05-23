# https://quera.ir/problemset/contest/4065/سؤال-خر-در-چمن-فراوونه

import math

inp = input().split(" ")
a, b, l = int(inp[0]), int(inp[1]), int(inp[2])
l_a = math.ceil(l/2)
l_b = l - l_a
print(l_a*a + l_b*b)
