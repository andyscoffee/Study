def solution(n, times):
    answer = 0
    mini = 1 # 심사에 필요한 최소 시간
    maxi = max(times)*n # 심사에 필요한 최대 시간
    
    while mini <= maxi:
        mid = (mini + maxi) // 2
        people = 0 # mid 시간만큼 심사한 사람의 수
        for time in times:
            people += (mid // time)
            if people >= n: # 더 많이 심사할 수 있다면 반복문 탈출
                break       
                
        if people >= n:
            answer = mid
            maxi = mid -1
            
        elif people < n:
            mini = mid +1
    return answer
