from collections import deque

def solution(n, vertex):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [-1]*(n+1)
    q = deque([1]) # 출발 도시(1) 시작
    distance[1] = 0
    
    for i in range(len(vertex)):
        a, b = vertex[i]
        graph[a].append((b))
        graph[b].append((a)) # 양방향 거리 1로 삽입
    
    while q: # BFS(모든 노드간의 거리가 1이기에))
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == -1:
                distance[i] = distance[now] + 1
                q.append(i)

    longest = max(distance) # 최대거리
    for i in range(1, n+1):
        if distance[i] == longest:
            answer += 1
    
    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, vertex))
