# 2231

import sys

N = int(sys.stdin.readline())
for i in range(N):
    data = list(map(int, str(i)))
    tmp = i + sum(data)
    if tmp == N:
        print(i)
        break
    if i == N-1:
        print(0)
