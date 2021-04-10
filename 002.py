"""
성적 계산하기 
반영비율과 받은 점수 입력
입력 순서 비율,시험 ....
비율은 실수,시험은 정수
"""

a_ratio,a_score=input("비율과 중간고사 점수를 입력하세요").split()
b_ratio,b_score=input("비율과 기말고사 점수를 입력하세요").split()
c_ratio,c_score=input("비율과 수행평가 점수를 입력하세요").split()

a_ratio=float(a_ratio)
b_ratio=float(b_ratio)
c_ratio=float(c_ratio)

a_score=int(a_score)
b_score=int(b_score)
c_score=int(c_score)

average=a_ratio*a_score + b_ratio*b_score + c_ratio*c_score

print('당신의 점수는',average)