# 16139

import sys

S = sys.stdin.readline().rstrip()
tmp = ''
prefix_sum = ['']
for i in S:
    tmp += i
    prefix_sum.append(tmp)
T = int(sys.stdin.readline())

for _ in range(T):
    a, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)
    cnt = 0
    query = (prefix_sum[r+1][l:r+1])
    for i in query:
        if a == i:
            cnt += 1
    print(cnt)
