n = int(input())


def sum(number):
    result = 0
    for s in str(number):
        result += int(s)
    return result


while int(n) >= 10:
    n = sum(n)
print(n)
