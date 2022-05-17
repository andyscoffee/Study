# 1753

import sys
import heapq


def dijk(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
INF = int(1e9)
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

dijk(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
