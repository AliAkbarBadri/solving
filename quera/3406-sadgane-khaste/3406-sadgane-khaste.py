# https://quera.ir/problemset/contest/3406/سؤال-پیاده-سازی-صدگان-خسته

inp1 = input()
inp2 = input()

number1 = int(inp1[::-1])
number2 = int(inp2[::-1])

output = ""

if number1 > number2:
    output = inp2 + " < "+inp1
elif number1 < number2:
    output = inp1 + " < "+inp2
else:
    output = inp2 + " = "+inp1

print(output)
