# 1181

import sys

n = int(sys.stdin.readline().strip())
data = set()
for i in range(n):
    data.add(sys.stdin.readline().strip())
data = list(data)
data.sort(key=lambda x: (len(x), x))

for i in data:
    print(i)
