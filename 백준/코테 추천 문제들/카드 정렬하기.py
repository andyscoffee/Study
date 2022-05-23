# 1715

import sys
import heapq

n = int(sys.stdin.readline())
data = []
ans = 0

for _ in range(n):
    heapq.heappush(data, int(sys.stdin.readline()))

while len(data) > 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    tmp = a+b
    ans += tmp
    heapq.heappush(data, tmp)

print(ans)
