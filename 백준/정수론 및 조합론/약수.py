# 1037
import sys

n = int(sys.stdin.readline())
div = list(map(int, sys.stdin.readline().split()))
if n == 1:
    print(pow(div[0], 2))
else:
    div.sort()
    print(div[0]*div[-1])
