# 10815

import sys

n = int(sys.stdin.readline())
data = set(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
qst = list(map(int, sys.stdin.readline().split()))
for q in qst:
    if q in data:
        print(1)
    else:
        print(0)
