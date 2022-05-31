# 1931

import sys

n = int(sys.stdin.readline())
data = []
cnt = 0

for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    data.append((s, e))
data.sort(key=lambda x: (x[1], x[0]))

end = 0
for t in data:
    s, e = t[0], t[1]
    if s >= end:
        cnt += 1
        end = e
print(cnt)
