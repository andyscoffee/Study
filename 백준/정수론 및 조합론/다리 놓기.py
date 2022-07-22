# 1010

import sys


def fac(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res


tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    if n == m:
        print(1)
        continue
    else:  # m개의 지역에 n개의 다리 -> mCn = m!/(m-n)!n!
        ans = fac(m)//(fac((m-n))*fac(n))
        print(ans)
