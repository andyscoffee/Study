# 11050

import sys


def factorial(x):
    if x == 0:
        return 1
    return factorial(x-1)*x


n, k = map(int, sys.stdin.readline().split())
print(factorial(n)//(factorial(k)*factorial(n-k)))
