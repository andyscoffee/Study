# 월간 코딩 챌린지 시즌 1

from itertools import combinations


def solution(numbers):
    answer = []
    tmp = list(combinations(numbers, 2))
    data = set()
    for num in tmp:
        data.add(sum(num))
    answer = list(sorted(data))
    return answer


print(solution([2, 1, 3, 4, 1]), [2, 3, 4, 5, 6, 7])
print(solution([5, 0, 2, 7]), [2, 5, 7, 9, 12])
