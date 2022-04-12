# 1436

import sys

n = int(sys.stdin.readline().strip())
hell = 666
cnt = 0
while True:
    if "666" in str(hell):
        cnt += 1
    if cnt == n:
        print(hell)
        break
    hell += 1
