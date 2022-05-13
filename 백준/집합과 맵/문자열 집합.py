# 14425

import sys

n, m = map(int, sys.stdin.readline().split())
data = []
cnt = 0

for _ in range(n):
    data.append(sys.stdin.readline().rstrip())
for _ in range(m):
    tmp = sys.stdin.readline().rstrip()
    if tmp in data:
        cnt += 1
print(cnt)
