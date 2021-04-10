'''
사주보기
태어난 연도,달,일 합친거에 100의 자리 숫자 홀짝인지 판별해 한다.
'''
year=int(input("출생연도: "))
month=int(input("출생달: "))
dat=int(input("출생일: "))

sum=int(year+month+dat)
luck=sum//100

if(luck%2==0):
    print("대박")
else:
    print("그럭저럭")




