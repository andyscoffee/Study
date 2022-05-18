# 24480

import sys
from collections import deque

n, m, start = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]
visited_cnt = [0]*(n+1)
cnt = 1
visited = [False]*(n+1)
st = deque()
st.append(start)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

while st:
    now = st.pop()
    visited[now] = True
    if visited_cnt[now] == 0:
        visited_cnt[now] = cnt
        cnt += 1
    for i in graph[now]:
        if not visited[i]:
            st.append(i)

for i in visited_cnt[1:n+1]:
    print(i)
