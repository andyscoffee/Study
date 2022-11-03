# 2477

import sys

K = int(sys.stdin.readline())
data = []
row = []
col = []
tmp = []  # 가장 긴 가로, 세로, 그와 인접한 변 저장
ans = 0
for _ in range(6):
    dir, meter = map(int, sys.stdin.readline().split())
    data.append((dir, meter))
    if dir == 3 or dir == 4:
        row.append((dir, meter))
    else:
        col.append((dir, meter))

max_col = max(col, key=lambda x: x[1])
max_row = max(row, key=lambda x: x[1])
for i in range(6):
    if data[i] == max_col or data[i] == max_row:
        tmp.append(data[(i+1) % 6])
        tmp.append(data[(i-1) % 6])

temp = 1
for v in data:
    if v not in tmp:  # 인접한 변이 아닌 두 변을 곱하면 전체 사각형에서 빈 사각형의 크기
        temp *= v[1]

ans = (max_col[1]*max_row[1]-temp)*K
print(ans)
