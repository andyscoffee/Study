# 124 나라의 숫자
def solution(n):
    answer = []
    while n:
        tmp = n % 3
        if tmp == 0:  # 0을 표시하지 않기 때문에 나누어 떨어진다면
            n -= 1  # 몫을 하나 낮춰
            tmp = 3  # 나머지를 3으로 저장함
        answer.append(str(tmp))
        n //= 3

    for i in range(len(answer)):
        if answer[i] == '3':
            answer[i] = '4'

    answer = ''.join(answer[::-1])
    return answer


for i in range(11):
    print(solution(i))
