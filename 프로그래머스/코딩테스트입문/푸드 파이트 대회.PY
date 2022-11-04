def solution(food):
    answer = ''
    for i in range(len(food)):
        if i == 0:
            continue
        if food[i] == 1:
            continue
        else:
            for j in range(food[i]//2):
                answer += str(i)
    tmp = ''.join(reversed(answer))
    answer = answer + '0' + tmp
    return answer


print(solution([1, 3, 4, 6]), "1223330333221")
print(solution([1, 7, 1, 2]), "111303111")
