# 2667

import sys

n = int(sys.stdin.readline())
graph = []
visited = [[False]*(n) for _ in range(n)]

for _ in range(n):
    tmp = list(input())
    graph.append(tmp)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global cnt
    visited[x][y] = True
    if graph[x][y] == '1':
        cnt += 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == '1':
                dfs(nx, ny)


cnt = 0
housing = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and visited[i][j] == False:
            dfs(i, j)
            housing.append(cnt)
            cnt = 0

housing.sort()
print(len(housing))
for i in housing:
    print(i)
