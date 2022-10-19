# 1644

import sys


def prime(n):
    data = [True for _ in range(n+1)]
    p = []
    for i in range(2, n+1):
        if data[i] == True:
            p.append(i)
            j = 2
            while i*j <= n:
                data[i*j] = False
                j += 1
    return p


N = int(sys.stdin.readline())
p_num = prime(N)
cnt, end = 0, 0
tmp = 0
for start in range(len(p_num)):
    while tmp < N and end < len(p_num):
        tmp += p_num[end]
        end += 1
    if tmp == N:
        cnt += 1
    tmp -= p_num[start]
print(cnt)
