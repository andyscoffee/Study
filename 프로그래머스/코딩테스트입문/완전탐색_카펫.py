def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    # 높이가 1,2인 경우에는 노란색을 감쌀 수 없음
    for h in range(3, total): 
        w = total // h
        if h*w == total and w>=h and (h-2)*(w-2) == yellow:
            answer.append(w)
            answer.append(h)
    return answer

brown = 24
yellow = 24
print(solution(brown, yellow))
