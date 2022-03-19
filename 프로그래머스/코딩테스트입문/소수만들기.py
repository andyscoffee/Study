# Summer/Winter Coding(~2018) 소수 만들기 (난이도 1)
from itertools import combinations
import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    data = list(combinations(nums, 3))
    for n in data:
        if is_prime(sum(n)):
            answer += 1

    return answer


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
