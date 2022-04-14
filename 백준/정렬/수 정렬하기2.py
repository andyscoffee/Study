# 2751 O(NlogN)
import heapq
import sys

n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    heapq.heappush(data, int(sys.stdin.readline().strip()))

for i in range(len(data)):
    print(heapq.heappop(data))
