# BOJ 5014[DFS+BFS 필수 문제]

import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
cnt = [0 for _ in range(F+1)]
visited = [0 for _ in range(F+1)]
UD = [U, -D]


def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        if now == G:
            return cnt[G]
        for i in range(2):
            nx = now + UD[i]
            if 0 < nx <= F and not visited[nx]:
                visited[nx] = 1
                cnt[nx] = cnt[now] + 1
                q.append(nx)
    if cnt[G] == 0:
        return 'use the stairs'


print(bfs(S))
