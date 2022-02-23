from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    tw = deque(truck_weights) # 대기 트럭
    moveon = [0] * bridge_length # 지나는 중인 트럭
    finished = deque() # 이미 다리를 지나간 트럭
    
    while len(finished) < len(truck_weights):
        answer += 1
        tmp = moveon.pop(0)
        
        if tmp != 0:
            finished.append(tmp)
        if tw: # 더 건너야 할 트럭이 존재한다면
            # 무게의 총 합이 한계 중량보다 더 적은지
            if sum(moveon)+tw[0] <= weight: 
                moveon.append(tw.popleft())# 다리를 건너기 시작
            else:
                moveon.append(0)
        """
        print(answer, '초')
        print('총 무게:',sum(moveon))
        print('대기 트럭',tw)
        print('지나는 중인 트럭',moveon)
        print('다 지나간 트럭',finished)
        """
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4, 5,6]
print(solution(bridge_length, weight, truck_weights))
