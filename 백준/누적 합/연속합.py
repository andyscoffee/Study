# 1912

import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    data[i] = max(data[i], data[i-1]+data[i])
print(max(data))
