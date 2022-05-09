# 10816

import sys
from bisect import bisect_left, bisect_right


def count_by_range(arr, left, right):
    ridx = bisect_right(arr, right)
    lidx = bisect_left(arr, left)
    return ridx-lidx


n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

m = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))

for i in tmp:
    answer = count_by_range(data, i, i)
    print(answer)
