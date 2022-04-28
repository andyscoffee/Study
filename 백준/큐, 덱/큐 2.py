# 18258

import sys
from collections import deque

n = int(sys.stdin.readline())
data = deque()
for _ in range(n):
    wtd = sys.stdin.readline().split()
    if len(wtd) > 1:
        data.append(wtd[1])
    elif wtd[0] == "pop":
        if data:
            print(data.popleft())
        else:
            print(-1)
    elif wtd[0] == "size":
        print(len(data))
    elif wtd[0] == "empty":
        if len(data) > 0:
            print(0)
        else:
            print(1)
    elif wtd[0] == "front":
        if data:
            print(data[0])
        else:
            print(-1)
    elif wtd[0] == "back":
        if data:
            print(data[-1])
        else:
            print(-1)
