# 1149

import sys

N = int(sys.stdin.readline())
data = []

for i in range(N):
    R, G, B = map(int, sys.stdin.readline().split())
    data.append([R, G, B])

for i in range(1, len(data)):
    data[i][0] = min(data[i-1][1], data[i-1][2])+data[i][0]
    data[i][1] = min(data[i-1][0], data[i-1][2])+data[i][1]
    data[i][2] = min(data[i-1][0], data[i-1][1])+data[i][2]

print(min(data[N-1][0], data[N-1][1], data[N-1][2]))
