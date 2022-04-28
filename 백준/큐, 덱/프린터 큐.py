# 1966

import sys
from collections import deque

tc = int(sys.stdin.readline())
for _ in range(tc):
    answer = 0
    num, loc = map(int, sys.stdin.readline().split())
    data = deque()
    priority = list(map(int, sys.stdin.readline().split()))
    ans = []

    for i in range(num):
        data.append((priority[i], i))

    while data:
        top = max(data)[0]
        if data[0][0] < top:
            data.append(data.popleft())
        else:
            ans.append(data.popleft()[1])

    for i in range(len(ans)):
        if ans[i] == loc:
            answer = i+1
    print(answer)
