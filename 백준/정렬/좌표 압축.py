# 18870
import sys

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
tmp = dict()
d_set = sorted(list(set(data)))

for i, value in enumerate(d_set):
    tmp[value] = i

for i in data:
    if i in tmp.keys():
        print(tmp[i], end=" ")
