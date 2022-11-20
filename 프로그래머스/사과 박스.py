def solution(k, m, score):
    answer = 0
    score.sort()
    while len(score) >= m:
        tmp = []
        for i in range(m):
            tmp.append(score.pop())
        answer += min(tmp)*m
    return answer


print(f'output:{solution(3, 4, 	[1, 2, 3, 1, 2, 3, 1])}', 'answer:8')
print(
    f'output:{solution(4, 3, 	[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])}', 'answer:33')
