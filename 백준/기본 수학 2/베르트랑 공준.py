# BOJ 4948
import math
import sys

arr = [True for i in range(246913)]
arr[1] = False
for i in range(2, 246913):
    if arr[i] == True:
        j = 2
        while i*j <= 246913:
            arr[i*j] = False
            j += 1
while True:
    n = int(sys.stdin.readline())
    cnt = 0
    if n == 0:
        break

    for i in range(n+1, 2*n+1):
        if arr[i] == True:
            cnt += 1
    print(cnt)
