# 24416

import sys


def fib_rec(n):
    global cnt_rec
    cnt_rec += 1
    if n == 1 or n == 2:
        cnt_rec -= 1
        return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)


"""
def fib_dyn(n):
    fib = [1]*(n+1)
    for i in range(3, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
의사 코드 구현
"""

N = int(sys.stdin.readline())
cnt_rec = 0
fib_rec(N)
print(cnt_rec+1, end=' ')
print(N-2)  # 동적 계획법상 n-2번 수행, 굳이 수행하지 않아도 결과를 알 수 있음
