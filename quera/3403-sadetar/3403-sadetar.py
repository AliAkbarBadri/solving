# https://quera.ir/problemset/contest/3403/سؤال-ساده-تر

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n_list = [n1, n2, n3, n4]

print("Sum : %.6f" % sum(n_list))
print("Average : %.6f" % (sum(n_list) / len(n_list)))
print("Product : %.6f" % (n1*n2*n3*n4))
print("MAX : %.6f" % max(n_list))
print("MIN : %.6f" % min(n_list))
