# https://quera.ir/problemset/contest/2886/سؤال-یک-ساعت

inp = input().split(" ")
mirror_hour, mirror_minute = int(inp[0]), int(inp[1])

real_hour = 12 - mirror_hour
real_minute = 60 - mirror_minute

if real_hour == 12:
    real_hour = "00"
elif real_hour < 10:
    real_hour = "0"+str(real_hour)
else:
    real_hour = str(real_hour)

if real_minute == 60:
    real_minute = "00"
elif real_minute < 10:
    real_minute = "0"+str(real_minute)
else:
    real_minute = str(real_minute)


print(real_hour+":"+real_minute)
