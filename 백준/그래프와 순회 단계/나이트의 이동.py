# 7562

import sys
from collections import deque


def bfs(L, a, b, c, d):
    q = deque()
    q.append([a, b])
    while q:
        nowx, nowy = q.popleft()
        if nowx == c and nowy == d:
            print(vstd[nowx][nowy])
            return
        for i in range(8):
            nx = nowx+dx[i]
            ny = nowy+dy[i]
            if 0 <= nx < L and 0 <= ny < L:
                vstd[nx][ny] = vstd[nowx][nowy]+1
                q.append([nx, ny])


TC = int(sys.stdin.readline())
for tc in range(TC):
    L = int(sys.stdin.readline())
    vstd = [[0]*L for _ in range(L)]
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    a, b = map(int, sys.stdin.readline().split())  # 시작
    c, d = map(int, sys.stdin.readline().split())  # 목적지
    bfs(L, a, b, c, d)

"""
투 포인터
n, target = map(~)
data = list(map(~))
end = 0, tmp = 0
for start in range(n):
    while start<n and target<target:
        tmp += data[i]
        end += 1
    if tmp == target:
        cnt += 1
    tmp -= data[start]
print(cnt)

def bfs(start):
    q = deque()
    q.append([start])
    while q:
        now = q.popleft()
        for i in range(4):
            nx = now + dx[i]
            if 0<=nx<N:
                dist[nx] = dist[now]+1
                q.append([nx])

def bin(arr, start, end, target):
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            end = mid-1
        else:
            start = mid +1
    return None
"""
