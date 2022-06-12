# 1021

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
needs = list(map(int, sys.stdin.readline().split()))
data = deque([i for i in range(1, n+1)])
cnt = 0

for i in needs:
    while True:
        if data[0] == i:
            data.popleft()
            break
        else:
            if data.index(i) < len(data)/2:
                while data[0] != i:
                    data.append(data.popleft())
                    cnt += 1
            else:
                while data[0] != i:
                    data.appendleft(data.pop())
                    cnt += 1
print(cnt)
