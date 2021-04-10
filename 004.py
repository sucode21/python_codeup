"""
비만도 측정하기
키와 몸무게 이용하여 비만도 측정
"""

height=int(input("키 입력: "))
weight=int(input("몸무게 입력: "))

if(height<150):
    measure=height-100
elif(height>=160):
    measure=(height-100)*0.9
else:
    measure=(height-150)/2 +50

wm=(weight-measure)*100/measure
print(wm)

if(wm<=10):
    print("정상")
elif(wm>20):
    print("비만")
else:
    print("과체중")

