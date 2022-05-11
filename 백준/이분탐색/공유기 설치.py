# 2110

import sys

n, c = map(int, sys.stdin.readline().split())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()
min_gap = 1  # start 역할, 공유기간 최단 거리차
max_gap = data[-1]-data[0]  # 공유기 사이 가능한 최장 거리
answer = 0

while (min_gap <= max_gap):
    gap = (min_gap + max_gap)//2
    tmp = data[0]
    cnt = 1
    for i in range(1, n):
        if data[i] >= tmp + gap:
            cnt += 1
            tmp = data[i]
    if cnt >= c:
        min_gap = gap + 1
        answer = gap
    else:
        max_gap = gap - 1
print(answer)
