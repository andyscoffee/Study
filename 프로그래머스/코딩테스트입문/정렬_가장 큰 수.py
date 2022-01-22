def solution(numbers):
    answer = ''
    n_nums = []
    for i, value in enumerate(numbers):
        n_nums.append([str(value)*3,i])
    n_nums.sort(reverse=True)

    for i in n_nums:
        answer += str(numbers[i[1]])
    
    for i in answer:
        if i != '0':
            return answer

    return '0'
