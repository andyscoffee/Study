# 카드 정렬하기 (핵심 유형)

import heapq

n = int(input())
res = 0
heap = []
for i in range(n):
    a = int(input())
    heapq.heappush(heap, a)
while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    res += a + b
    heapq.heappush(heap, res)
print(res)
