"""
이 달은 며칠까지 있을까

if(year%400==0):
        print(29)
    elif(year%100==0):
        print(28)
    elif(year%4==0):
        print(29):
    else:
        print(28)
"""
year=int(input("년도를 입력하세요: "))
month=int(input("달을 입력하세요: "))

if(month<8):
    if(month==2):
        if(year%400==0):
            print(29)
        elif(year%100==0):
            print(28)
        elif(year%4==0):
            print(29)
        else:
            print(28)
    elif(month%2==0):
        print(30)
    else:
        print(31)
else:
    if(month%2==0):
        print(31)
    else:
        print(30)
