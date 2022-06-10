# 1197

import sys


def fp(parent, x):
    if parent[x] != x:
        parent[x] = fp(parent, parent[x])
    return parent[x]


def up(parent, a, b):
    a = fp(parent, a)
    b = fp(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())
parent = [0]*(v+1)
edges = []
res = 0
for i in range(1, v+1):
    parent[i] = i
for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))
edges.sort()
for edge in edges:
    cost, a, b = edge
    if fp(parent, a) != fp(parent, b):
        up(parent, a, b)
        res += cost
print(res)
