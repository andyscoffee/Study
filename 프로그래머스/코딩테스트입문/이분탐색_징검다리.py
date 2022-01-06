def solution(distance, rocks, n):
    answer = 0
    start = 0
    end = distance
    rocks.sort()
    
    while start <= end:
        mid = (start + end) // 2
        diff = 0 #최솟값을 저장할 변수
        current = 0 #비교를 위한 현재 위치 변수
        cnt = 0 # 제거한 돌의 수
        for rock in rocks:
            diff = rock - current # 돌 간의 거리
            if diff < mid:
                cnt += 1
            else:
                current = rock
            if cnt > n:
                break
        if cnt > n:
            end = mid -1
        else:
            answer = mid
            start = mid +1
            
    return answer
