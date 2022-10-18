# 1697

import sys
from collections import deque


def BFS(start):
    q = deque([start])
    while q:
        now = q.popleft()
        if now == k:
            print(vstd[now])
            break
        for i in route:
            if i == -1 or i == 1:
                nx = now+i
                if 0 <= nx < MAX and not vstd[nx]:
                    vstd[nx] = vstd[now] + 1
                    q.append(nx)
            else:
                nx = now * i
                if 0 <= nx < MAX and not vstd[nx]:
                    vstd[nx] = vstd[now] + 1
                    q.append(nx)
    return


n, k = map(int, sys.stdin.readline().split())
MAX = (10**5)
vstd = [0]*MAX  # 100,000 까지
route = [-1, 1, 2]  # x-1, x+1, x*2
BFS(n)
