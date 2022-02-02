def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        if count_div(i) < 0:
            answer -= i
        else:
            answer += i
    
    return answer

def count_div(n):
    cnt = 0
    for i in range(1, n+1):
        if n%i == 0:
            cnt+=1

    if cnt % 2 == 0:
        return cnt
    else:
        return -cnt
