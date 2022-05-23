# 1655

import heapq
import sys

n = int(sys.stdin.readline())
left_h = []
right_h = []
ans = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if len(left_h) == len(right_h):
        heapq.heappush(left_h, (-x, x))
    else:
        heapq.heappush(right_h, (x, x))
    if right_h and left_h[0][1] > right_h[0][0]:
        min = heapq.heappop(right_h)[0]
        max = heapq.heappop(left_h)[1]
        heapq.heappush(left_h, (-min, min))
        heapq.heappush(right_h, (max, max))
    ans.append(left_h[0][1])

for i in ans:
    print(i)
