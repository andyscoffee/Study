# 월간 코드 챌린지 시즌 3 나머지가 1이 되는 수 찾기 (난이도 1)
def solution(n):
    answer = 0
    for i in range(1, 1000000):
        if n % i == 1:
            answer = i
            break
    return answer
