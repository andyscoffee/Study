# 7576

import sys
from collections import deque


def bfs():
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:  # 익지 않은 토마토일 경우만
                    graph[nx][ny] = graph[a][b] + 1
                    q.append((nx, ny))


M, N = map(int, sys.stdin.readline().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
ans = 0
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))

bfs()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(graph[i]))
print(ans-1)
