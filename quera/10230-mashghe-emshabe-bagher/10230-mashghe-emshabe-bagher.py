# https://quera.ir/problemset/contest/10230/سؤال-مشق-امشب-باقر

n = input()
angles = n.split(" ")
result = "No"
if int(angles[0]) and int(angles[1]) and int(angles[2]) and int(angles[0])+int(angles[1])+int(angles[2]) == 180:
    result = "Yes"
print(result)
