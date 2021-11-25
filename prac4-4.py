# 게임 개발

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
check = [[0] * m for _ in range(n)]  # 방문 체크를 위한 리스트 선언
check[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))  # 맵 입력 받기

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():  # 왼쪽으로 도는 함수 정의
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


cnt = 1
turn = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if check[nx][ny] == 0 and array[nx][ny] == 0:  # 육지이고 가보지 않았던 곳이라면 이동
        x = nx
        y = ny
        check[nx][ny] = 1
        cnt += 1
        turn = 0
        continue
    else:  # 회전 이후 육지가 아니거나 가본 곳 이라면
        turn += 1
    if turn == 4:  # 4방향 모두 갈 수 없는 경우
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:  # 뒤가 바다
            break
        turn = 0
print(cnt)
