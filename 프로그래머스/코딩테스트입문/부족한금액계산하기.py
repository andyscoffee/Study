# 위클리 챌린지 부족한 금액 계산하기 (난이도 1)
def solution(price, money, count):

    tmp = 0
    for i in range(1, count+1):
        tmp += price * i
    if money - tmp >= 0:
        print(tmp)
        return 0

    return abs(money-tmp)
