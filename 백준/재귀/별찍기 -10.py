# 2447
import sys


def star(n):
    if n == 1:
        return ["*"]
    s = star(n//3)
    l = []
    for i in s:
        l.append(i*3)
    for i in s:
        l.append(i+" "*(n//3)+i)
    for i in s:
        l.append(i*3)
    return l


n = int(sys.stdin.readline().strip())
print("\n".join(star(n)))
