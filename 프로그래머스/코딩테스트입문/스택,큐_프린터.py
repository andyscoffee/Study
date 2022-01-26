from collections import deque

def solution(priorities, location):
    answer = 0
    tmp = deque() # (우선 순위, 원 순서) 큐
    res = [] # 작업 순서를 저장할 리스트
    for i in range(len(priorities)):
        tmp.append((priorities[i],i))
   
    
    while tmp:
        top = max(tmp)[0] # 우선 순위가 가장 높은 작업
        if tmp[0][0] < top: # 현재 작업(맨 앞) 보다 우선 순위가 높은 작업이 있을 경우
            tmp.append(tmp.popleft()) # 큐의 맨 뒤로 보냄
        # 현재 작업의 우선 순위가 가장 높거나 같은 경우 작업 수행, 순서 리스트에 저장
        else:
            res.append(tmp.popleft()[1]) 

    for i in range(len(res)):
        if res[i] == location:
            answer = i+1
    return answer

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))
