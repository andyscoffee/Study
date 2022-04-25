# 10773

import sys

data = [0]
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        data.pop()
    else:
        data.append(num)
print(sum(data))
