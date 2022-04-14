# 11650

import sys

n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))
data = sorted(data, key=lambda x: (x[0], x[1]))
for a, b in data:
    print(a, b)
