def solution(number, limit, power):
    answer = 0
    data = []
    for n in range(1, number+1):
        tmp = 0
        for i in range(1, int(n**(1/2))+1):
            if n % i == 0:
                tmp += 1
                if ((i**2) != n):
                    tmp += 1
        data.append(tmp)
    for d in data:
        if d <= limit:
            answer += d
        else:
            answer += power
    return answer


print(f'output:{solution(5, 3, 2)}', 'answer:10')
print(f'output:{solution(10, 3, 2)}', 'answer:21')
