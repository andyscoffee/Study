# 1927

import heapq
import sys

n = int(sys.stdin.readline())
h = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, x)
