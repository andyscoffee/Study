# 다익스트라 알고리즘 한 지점에서 다른 특정 지점까지의 최단 경로 구하기

import sys
import heapq  # 우선순위 큐 사용

input = sys.stdin.readline  # 빠른 읽기
INF = int(1e9)  # 무한 정의

n, m = map(int, input().split())  # 노드, 간선의 수 입력
start = int(input())  # 시작 지점 입력
graph = [[] for i in range(n + 1)]  # 노드 정보 담기 위한 그래프 초기화
distance = [INF] * (n + 1)  # 최단 거리 담기위한 리스트 초기화

for _ in range(m):
    a, b, c = map(int, input().split())  # a노드->b노드 거리는 c
    graph[a].append((b, c))  # 노드 정보에 삽입


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0  # 시작 노드와의 거리는 0, 큐에 삽입
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
