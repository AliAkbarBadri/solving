# https://quera.ir/problemset/contest/3404/سؤال-تو-چقدر-اضافه-وزن-داری

weight = int(input())
height = float(input())

bmi = weight / (height**2)
status = ""
if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print("%.2f" % bmi)
print(status)
