from itertools import combinations


def solution(arr, K):
    answer = 0
    data = list(combinations(arr, 3))
    for d in data:
        if sum(d) % 3 == 0:
            answer += 1

    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
