# 4386

import sys
import math
sys.setrecursionlimit(10**6)


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


n = int(sys.stdin.readline())
parent = [i for i in range(n+1)]
data = []
edges = []
res = 0

for _ in range(n):
    a, b = map(float, sys.stdin.readline().split())
    data.append((a, b))

for i in range(n-1):
    for j in range(i+1, n):
        edges.append(
            (math.sqrt((data[i][0] - data[j][0])**2 + (data[i][1] - data[j][1])**2), i, j))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if fp(parent, a) != fp(parent, b):
        up(parent, a, b)
        res += cost

print(round(res, 2))
