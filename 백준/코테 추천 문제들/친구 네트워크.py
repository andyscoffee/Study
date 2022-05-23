# 4195

import sys


def up(parent, a, b):
    a = fp(parent, a)
    b = fp(parent, b)
    if a != b:
        parent[b] = a
        number[a] += number[b]


def fp(parent, x):
    if parent[x] != x:
        parent[x] = fp(parent, parent[x])
    return parent[x]


T = int(sys.stdin.readline())
for tc in range(T):
    n = int(sys.stdin.readline())
    parent = dict()
    number = dict()

    for _ in range(n):
        a, b = sys.stdin.readline().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        up(parent, a, b)
        print(number[fp(parent, a)])
