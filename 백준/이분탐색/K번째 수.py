# 1300
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = k
res = 0

while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(n, int(mid/i))
    if cnt >= k:
        res = mid
        end = mid - 1
    else:
        start = mid + 1
print(res)
