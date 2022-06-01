# 2470

import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

close = 2e9
start, end = 0, n-1
data.sort()
ans = []
while start < end:
    tmp = data[start]+data[end]
    if tmp == 0:
        ans = [data[start], data[end]]
        break
    if abs(tmp) < close:
        close = abs(tmp)
        ans = [data[start], data[end]]
    if tmp < 0:
        start += 1
    else:
        end -= 1

print(*ans)
