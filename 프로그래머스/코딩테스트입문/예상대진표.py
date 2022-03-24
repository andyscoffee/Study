def solution(n, a, b):
    answer = 1
    while True:
        if (a % 2 != 0 and a+1 == b) or (a % 2 == 0 and a-1 == b):
            return answer
        a = div(a)
        b = div(b)
        answer += 1


def div(x):
    if x % 2 == 0:
        return x//2
    else:
        return x//2 + 1


print(solution(8, 4, 5), 3)
print(solution(16, 7, 15), 4)
print(solution(32, 30, 31), 2)
print(solution(64, 64, 63), 1)
print(solution(8, 1, 7), 3)
print(solution(8, 2, 3), 2)
print(solution(8, 4, 7), 3)
