# 없는 숫자 더하기 (월간 코드 챌린지 시즌3)
def solution(numbers):
    answer = 0
    i = 0
    while i<10:
        if i not in numbers:
            answer += i
        i += 1
    return answer
