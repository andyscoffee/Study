def solution(number, k):
    num = list(number)
    tmp = 0
    i = 0
    check = len(num)
    check2 = k
    while k > 0:
        if i+1 == len(num):
            break
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
    
    if len(num)>check-check2:
        for i in range(k):
            del num[-1]
    
    return ''.join(num)

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))

print(solution("87654321", 3))
print(solution("18765432", 3))
print(solution("77413258", 2))
print(solution("12345678901234567890", 19))
print(solution("01010", 3))
print(solution("559913", 1))
print(solution("9191919", 1))
"""
"87654321", 3, "87654"
"18765432", 3, "87654"
"77413258", 2, "774358"
"12345678901234567890", 19, "9"
"01010", 3, "11"
"559913", 1, "59913"
"9191919", 1, "991919"
"""
