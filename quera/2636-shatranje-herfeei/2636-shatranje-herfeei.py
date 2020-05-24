# https://quera.ir/problemset/contest/2636/سؤال-شطرنج-حرفهای

import numpy as np

main = [1, 1, 2, 2, 2, 8]
inp = [int(x) for x in input().split(" ")]
output = [str(a_i - b_i) for a_i, b_i in zip(main, inp)]
print(" ".join(output))
