# 1654

import sys


def bin(target, arr, start, end):
    answer = 0
    while (start <= end):
        cnt = 0
        mid = (start + end)//2
        for i in arr:
            if mid == 0:
                return answer
            cnt += i//mid
        if cnt < target:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer


k, n = map(int, sys.stdin.readline().split())
data = []
for _ in range(k):
    data.append(int(sys.stdin.readline()))
print(bin(n, data, 1, max(data)))
