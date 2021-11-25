# 왕실의 나이트

start = input()
row = int(start[1])
col = int(ord(start[0])) - 96
cnt = 0

ways = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for way in ways:
    now_row = row + way[0]
    now_col = col + way[1]
    if now_col >= 1 and now_col <= 8 and now_row >= 1 and now_row <= 8:
        cnt += 1
print(cnt)
