# 뱀 (삼성전자 SW 역량테스트)

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1  # 사과의 위치 1로 표시

info = []
l = int(input())
for _ in range(l):
    t, d = input().split()
    info.append((int(t), d))

dx = [0, 1, 0, -1]  # 오른쪽 바라보고 있기에 동-남-서-북 순서
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulation():
    x, y = 1, 1
    data[x][y] = 2  # 뱀의 머리 위치 2로 표시
    direction = 0  # 시작시 오른쪽(동쪽)을 바라보고 있음
    time = 0
    index = 0
    q = [(x, y)]  # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx>=1 and ny>=1 and nx<=n and ny<=n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time


print(simulation())
