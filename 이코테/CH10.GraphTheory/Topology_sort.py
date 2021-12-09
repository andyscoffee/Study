# 위상 정렬
from collections import deque
  
v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

def topology_sort():
  res = 0
  q = deque()
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    res.append(now)
    for i in graph[now]:
      indegree[i] -= 1 # 연결 노드 진입 차수 1씩 감소
      if indegree[i] == 0:
        q.append(i)
  for i in res:
    print(i, end = ' ')

topology_sort()