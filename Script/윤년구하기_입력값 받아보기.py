year = 2020

if (year % 4 == 0) and (year % 100 != 0):
    print(year, "는 윤년입니다.")
elif year % 400 == 0:
    print(year, "는 윤년입니다.")
else:
    print(year, "는 윤년이 아닙니다")

n = 3
while n >= 0:
    m = input("Enter a integer: ")
    if int(m) == 0: break
    n = n - 1
else:
    print("4 inputs.")

kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum1, sum2, sum3, sum4 = 0, 0, 0, 0

for i in range(0, 5):
    sum1 = sum1 + kor[i] + eng[i]

print('sum1=', sum1)
