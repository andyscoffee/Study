# 1012

import sys
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(a, b):
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if (0 <= nx < N) and (0 <= ny < M):
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx, ny)

    return


TC = int(sys.stdin.readline())
for t in range(TC):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*(M) for _ in range(N)]
    ans = 0
    for _ in range(K):
        i, j = map(int, sys.stdin.readline().split())
        graph[j][i] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(i, j)
                ans += 1
    print(ans)
