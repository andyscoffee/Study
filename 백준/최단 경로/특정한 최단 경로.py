# 1504

from curses.ascii import NL
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


n, m = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]
INF = int(1e9)
distance = [INF]*(n+1)


def bin(arr, target, start, end):
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        end = mid - 1
    else:
        start = mid+1
    return False
