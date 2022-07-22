# 7576

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b + dy[i]
            if nx <= 0 or ny <= 0 or nx > N or ny > M:
                if graph[nx][ny] == 0:  # 벽인 경우
                    graph[nx][ny] = graph[a][b]+1
                    q.append((nx, ny))
    return graph[N-1][M-1]


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            print()
