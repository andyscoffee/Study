from collections import deque

def solution(progresses, speeds):
    answer = []
    d_date = [] # 배포 날짜를 저장
    p_q = deque(progresses) # 작업 큐
    s_q = deque(speeds) # 속도 큐
    
    n = 0 # 배포까지 걸리는 날짜를 세기 위한 변수
    while p_q:
        if s_q[0]*n + p_q[0] >= 100: # 첫번째 기능의 진행도가 100 이상이라면 
            p_q.popleft() # 배포
            s_q.popleft()
            d_date.append(n) # 배포 날짜 저장
            if p_q: # 다음 배포해야할 기능이 남아 있을 떄
                if s_q[0]*n + p_q[0] >= 100: # 다음으로 배포할 기능의 진행도가 100 이상이라면 
                    p_q.popleft() # 배포
                    s_q.popleft()
                    d_date.append(n)
        else:
            n += 1 # 하루 증가

    for i in range(len(d_date)-1):
        if i == 0: # 첫 배포는 최소 하나의 기능이 있기에 
            answer.append(1)
        if d_date[i] == d_date[i+1]: # 배포 날짜가 같다면
            answer[-1]+=1 # 마지막 배포 시기에 배포하는 기능 1 증가
        else:
            answer.append(1) # 같지 않은 경우 따로 배포
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
