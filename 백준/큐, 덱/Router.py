# BOJ 15825

import sys
from collections import deque

N = int(sys.stdin.readline())
h = deque()
while True:
    p = int(sys.stdin.readline())
    if p == -1:
        break
    if p == 0:
        h.popleft()
        continue
    if len(h) == N:
        continue
    h.append(p)
if h:
    print(*h)
else:
    print('empty')
