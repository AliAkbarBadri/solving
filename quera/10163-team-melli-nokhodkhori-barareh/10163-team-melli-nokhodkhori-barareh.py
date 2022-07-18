# https://quera.ir/problemset/contest/10163/سؤال-تیم-ملی-نخودخوری-در-برره

inp = input().split(" ")
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])


def get_range():
    inp = input().split(" ")
    start, end = int(inp[0]), int(inp[1])
    return start, end, range(start, end)


start1, end1, range1 = get_range()
start2, end2, range2 = get_range()
start3, end3, range3 = get_range()
min_start = min([start1, start2, start3])
max_end = max([end1, end2, end3])
for i in range(min_start, max_end):
    if i in range1:
        if i in range2:
