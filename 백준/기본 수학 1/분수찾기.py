# 1193

import sys

n = int(sys.stdin.readline())
line, max_n = 0, 0

while n > max_n:
    line += 1
    max_n += line
gap = max_n - n

if line % 2 == 0:  # 짝수 라인일 때
    top = line - gap
    bottom = gap + 1
else:
    top = gap + 1
    bottom = line - gap

print(str(top)+'/'+str(bottom))
