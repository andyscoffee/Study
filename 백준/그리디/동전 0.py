# 11047

import sys
from collections import deque

coins = deque()
n, k = map(int, sys.stdin.readline().split())
cnt = 0
for _ in range(n):
    coins.appendleft(int(sys.stdin.readline()))

for i in coins:
    cnt += k//i
    k %= i
print(cnt)
