# 3273

import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
cnt = 0
start, end = 0, n-1
data.sort()
while start != end:
    if data[start]+data[end] == x:
        cnt += 1
        start += 1
    elif data[start]+data[end] > x:
        end -= 1
    else:
        start += 1
print(cnt)
