# 11725

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[]for _ in range(n+1)]
parent = [-1]*(n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(n):
    for i in graph[n]:
        if parent[i] == -1:
            parent[i] = n
            dfs(i)


dfs(1)
for i in range(2, n+1):
    print(parent[i])
