# 24445

import sys
from collections import deque


def BFS(graph, start, visited):
    global cnt
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        visited_cnt[v] = cnt
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


n, m, start = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]
visited_cnt = [0]*(n+1)
cnt = 1
visited = [False]*(n+1)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort(reverse=True)

BFS(graph, start, visited)

for i in visited_cnt[1:n+1]:
    print(i)
