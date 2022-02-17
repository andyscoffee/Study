def solution(s):
    s = list(s)
    tmp = []
    
    for i in range(len(s)):
        if not tmp:
            tmp.append(s[i])
        elif tmp[-1] == s[i]:
            tmp.pop()
        else:
            tmp.append(s[i])
    if tmp:
        return 0
    else:
        return 1

s = "baab"
print(solution(s))
