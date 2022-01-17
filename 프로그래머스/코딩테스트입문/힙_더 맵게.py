import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) <2:
            return -1
        least = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = least + (second * 2)
        heapq.heappush(scoville, mixed)
        answer += 1
    if answer == 0:
        return -1
    
    return answer
