# 24479

import sys
from collections import deque
"""
# 테스트 케이스 예시는 맞는데 제출 시 재귀 에러 뜸
def DFS(graph, visited, v): 
    visited[v] = True
    global cnt
    visited_cnt[v] = cnt
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, visited, i)
"""
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
    graph[i].sort(reverse=True)

# DFS(graph, visited, start) 프로그래머스 recursion 에러

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
