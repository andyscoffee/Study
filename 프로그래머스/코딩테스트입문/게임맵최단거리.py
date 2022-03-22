# 찾아라 프로그래밍 마에스터
from collections import deque


def solution(maps):
    q = deque([(0, 0)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    m = len(maps[0])
    n = len(maps)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    answer = maps[n-1][m-1]
    if maps[n-1][m-1] == 1:
        return -1
    return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]), -1)
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]), 11)
