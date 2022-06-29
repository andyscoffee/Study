# 2292

import sys

n = int(sys.stdin.readline())
honeycomb = 1
cnt = 1
while n > honeycomb:
    honeycomb += 6*cnt
    cnt += 1
print(cnt)
