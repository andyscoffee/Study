# 13549

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
distance = [-1]*100001


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        time, now = heapq.heappop(q)
        if now == k:
            return distance[now]
        for i in range(3):  # -1, +1, *2 3가지 경우의 수
            if i == 0:
                nx = now - 1
            elif i == 1:
                nx = now + 1
            else:
                nx = now*2
            if nx <= 0 or nx > 100001:
                continue
            if distance[nx] != -1 and distance[nx] <= distance[now]:
                continue
            if i < 2:
                heapq.heappush(q, (time+1, nx))
                distance[nx] = time + 1
            else:
                heapq.heappush(q, (time, nx))
                distance[nx] = time


print(dijkstra(n))
