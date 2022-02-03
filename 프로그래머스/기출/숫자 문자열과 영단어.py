def solution(s):
    answer = ''
    number = ''
    num = {'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'}

    for i in s:
        if i.isdigit():
            answer += i
        else:
            number += i

        if number in num:
            answer += num[number]
            number = ''
    
    return int(answer)

s = "one4seveneight"
print(solution(s))
