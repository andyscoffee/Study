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


tc = int(input())
for t in range(tc):
    n, m = map(int, input().split())
    parent = [0]*(n+1)
    edges = []
    res = 0
    for i in range(1, n+1):
        parent[i] = i

    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((1, a, b))
    edges.sort()
    for edge in edges:
        cost, a, b = edge
        if fp(parent, a) != fp(parent, b):
            up(parent, a, b)
            res += cost
