# 20040

import sys


def find_parents(parent, x):
    if parent[x] != x:
        parent[x] = find_parents(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parents(parent, a)
    b = find_parents(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
cycle = False
ans = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if cycle:
        continue
    if find_parents(parent, a) == find_parents(parent, b):
        if not cycle:
            ans = i + 1
            cycle = True
    else:
        union_parent(parent, a, b)

print(ans)
