# BOJ 2581
import math
import sys


m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
tmp = 0
mp = 10001
arr = [True for i in range(n+1)]
arr[1] = False
for i in range(2, int(math.sqrt(n)+1)):
    if arr[i] == True:
        j = 2
        while i*j <= n:
            arr[i*j] = False
            j += 1
for i in range(m, n+1):
    if arr[i]:
        tmp += i
        mp = min(mp, i)
if tmp:
    print(tmp)
    print(mp)
else:
    print(-1)
