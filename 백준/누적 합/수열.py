# 2559

import sys

n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
res = []
res.append(sum(data[:k]))
for i in range(n-k):
    res.append(res[i]-data[i]+data[i+k])
print(max(res))
