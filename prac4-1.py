# 상하좌우

n = int(input())
x, y = 1, 1
ways = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
arrow = ["L", "R", "U", "D"]

for way in ways:
    for i in range(len(arrow)):
        if way == arrow[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny
print(x, y)
