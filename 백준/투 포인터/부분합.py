# 1806

import sys

n, s = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
start, end = 0, 1
temp = data[0]+data[end]
while start < end:
    tmp = data[start]+data[end]
    if tmp > s:
        print()
