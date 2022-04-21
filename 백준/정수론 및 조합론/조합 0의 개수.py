# 2004
import sys


def cnt_2(x):
    cnt = 0
    while x > 0:
        x //= 2
        cnt += x
    return cnt


def cnt_5(x):
    cnt = 0
    while x > 0:
        x //= 5
        cnt += x
    return cnt


def cnt_0(x, y):
    a = cnt_2(x)-cnt_2(y)-cnt_2(x-y)
    b = cnt_5(x)-cnt_5(y)-cnt_5(x-y)
    return min(a, b)


n, k = map(int, sys.stdin.readline().split())
print(cnt_0(n, k))
