# 10968

import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
tmp, end = 0, 0
cnt = 0
for start in range(n):
    while tmp < m and end < n:
        tmp += data[end]
        end += 1
    if tmp % m == 0:
        cnt += 1
    tmp -= data[start]
print(cnt)
