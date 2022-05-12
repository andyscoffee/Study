# 12015

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = [0]

for i in arr:
    if ans[-1] < i:
        ans.append(i)
    else:
        start = 0
        end = len(ans)
        while start < end:
            mid = (start+end)//2
            if ans[mid] < i:
                start = mid+1
            else:
                end = mid
        ans[end] = i
print(len(ans)-1)
