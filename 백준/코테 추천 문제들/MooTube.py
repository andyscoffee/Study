# 15591

import sys
from collections import deque

N, Q = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, usado = map(int, sys.stdin.readline().split())
    graph[a].append((b, usado))
    graph[b].append((a, usado))

for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    visited = [False for _ in range(N+1)]
    visited[v] = True
    ans = 0
    q = deque([(v, 1e9)])
    while q:
        now, usado = q.pop()
        for connected, newsado in graph[now]:
            newsado = min(usado, newsado)
            if newsado >= k and not visited[connected]:
                ans += 1
                visited[connected] = True
                q.append((connected, newsado))
    print(ans)
