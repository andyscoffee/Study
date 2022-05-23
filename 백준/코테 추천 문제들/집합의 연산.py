# 1717

import sys
sys.setrecursionlimit(10**6)


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
parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    do, a, b = map(int, sys.stdin.readline().split())
    if do == 0:
        union_parent(parent, a, b)
    elif do == 1:
        x = find_parents(parent, a)
        y = find_parents(parent, b)
        if x == y:
            print('YES')
        else:
            print('NO')
