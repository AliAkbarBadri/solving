# https://quera.ir/problemset/contest/17675/سؤال-رشته-فیبوناچی

inp = int(input())


def fib(x):
    fib_list = [1, 2]
    for i in range(2, x+1):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list


output = ""
fib_list = fib(inp)
for i in range(1, inp+1):
    if i in fib_list:
        output += "+"
    else:
        output += "-"

print(output)
