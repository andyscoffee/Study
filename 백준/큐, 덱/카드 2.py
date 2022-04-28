# 2164

import sys
from collections import deque

n = int(sys.stdin.readline())
data = deque([i for i in range(n, 0, -1)])

while len(data) > 1:
    data.pop()
    data.appendleft(data.pop())

print(*data)
