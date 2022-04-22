# 11659
import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
tmp = 0
prefix_sum = [0]

for i in data:
    tmp += i
    prefix_sum.append(tmp)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(prefix_sum[b]-prefix_sum[a-1])
