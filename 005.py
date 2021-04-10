"""
영어 서수로 표현하기
"""

num=int(input("숫자를 입력하세요"))

check=num%100

if(check==11,12,13):
    print("%d th"%num)
else:
    check=check%10
    if(check==1):
        print("%d st"%num)
    elif(check==2):
        print("%d nd" %num)
    elif(check==3):
        print("%d rd"%num)
    else:
        print("%d th"%num)



