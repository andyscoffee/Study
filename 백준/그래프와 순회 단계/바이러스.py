# 2606

import sys
from collections import deque


def DFS(graph, visited, v):
    visited[v] = True
    global cnt
    visited_cnt[v] = cnt
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, visited, i)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
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

DFS(graph, visited, 1)
tmp = -1
for i in visited_cnt:
    if i != 0:
        tmp += 1
print(tmp)
