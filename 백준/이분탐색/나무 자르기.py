# 2805

import sys


def bin(target, arr, start, end):
    answer = 0
    while (start <= end):
        total = 0
        mid = (start + end)//2
        for i in arr:
            if i > mid:
                total += i-mid
        if total < target:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer


n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
print(bin(m, data, 1, max(data)))
