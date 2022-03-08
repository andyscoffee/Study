def solution(number, k):
    num = list(number)
    tmp = 0
    i = 0
    
    while k > 0:
        if tmp == 0:
            tmp = num[i]
            continue
        if tmp < num[i+1]:
            tmp = num[i+1]
            del num[i]
            i = 0
            k -= 1
            continue
        else:
            tmp = num[i+1]
        i += 1
        
    return ''.join(num)

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
