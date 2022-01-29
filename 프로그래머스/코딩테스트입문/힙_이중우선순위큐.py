import heapq as hq

def solution(operations):
    answer = []
    min_h = []
    max_h = []
    
    for i in range(len(operations)):
        oper, num = operations[i].split()
        if oper == "I":
            hq.heappush(min_h, int(num))
            hq.heappush(max_h, -int(num))
        elif max_h and num == "1":
            hq.heappop(max_h)
            min_h.pop()
        elif min_h and num == "-1":
            hq.heappop(min_h)
            max_h.pop()
    
    if max_h:
        answer.append(-(hq.heappop(max_h)))
        answer.append(hq.heappop(min_h))
    else:
        return [0,0]
    
    return answer
