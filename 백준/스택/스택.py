# 10828

import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    wtd = sys.stdin.readline().split()
    if len(wtd) > 1:
        data.append(wtd[1])
    elif wtd[0] == "pop":
        if data:
            print(data.pop())
        else:
            print(-1)
    elif wtd[0] == "size":
        print(len(data))
    elif wtd[0] == "empty":
        if len(data) >= 1:
            print(0)
        else:
            print(1)
    elif wtd[0] == "top":
        if data:
            print(data[-1])
        else:
            print(-1)
