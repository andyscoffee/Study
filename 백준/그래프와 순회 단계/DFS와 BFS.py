# 1260

import sys
from collections import deque


def DFS(v):
    vstd_dfs[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not vstd_dfs[i]:
            DFS(i)


def BFS(start):
    q = deque([start])
    vstd_bfs[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not vstd_bfs[i]:
                q.append(i)
                vstd_bfs[i] = True


n, m, start = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]
vstd_dfs = [False]*(n+1)
vstd_bfs = [False]*(n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

DFS(start)
cnt = 1
print()
BFS(start)
