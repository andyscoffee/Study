# BOJ 1929
import math
import sys

m, n = map(int, sys.stdin.readline().split())
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
        print(i)
