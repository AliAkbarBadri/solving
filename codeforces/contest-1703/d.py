# https://codeforces.com/contest/1703/problem/D

n_test_cases = int(input())
 
for _ in range(n_test_cases):
    n_str = int(input())
    str_list = []
    for i in range(n_str):
        str_list.append(input())
    str_set = set(str_list)
    result = ""
    for item in str_list:
        is_exist = False
        for i in range(1, len(item)):
            if item[:i] in str_set and item[i:] in str_set:
                is_exist = True
        if is_exist:
            result += "1"
        else:
            result += "0"
    print(result)