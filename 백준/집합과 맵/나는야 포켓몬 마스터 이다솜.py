# 1620

import sys

n, m = map(int, sys.stdin.readline().split())
pokedex = dict()
for i in range(1, n+1):
    tmp = sys.stdin.readline().rstrip()
    pokedex[i] = tmp
    pokedex[tmp] = i

for _ in range(m):
    q = sys.stdin.readline().rstrip()
    if not q.isalpha():
        print(pokedex[int(q)])
    else:
        print(pokedex[q])
