#커리큘럼

from collections import deque
import copy

v = int(input())
indegree = [0]*(v+1)
graph = [[] for i in range(v+1)]
time = [0]*(v+1)

for i in range(1, v+1):
  data = list(map(int, input().split()))
  time[i] = data[0]
  for j in data[1:-1]:
    indegree[i] +=1
    graph[j].append(i)

def topology_sort():
  res = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
  q = deque()

  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()

    for i in graph[now]:
      res[i] = max(res[i], res[now]+time[i])
      indegree[i] -= 1 # 연결 노드 진입 차수 1씩 감소
      if indegree[i] == 0:
        q.append(i)

  for i in range(1, v+1):
    print(res[i])

topology_sort()