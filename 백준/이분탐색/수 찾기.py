# 1920

import sys


def bin(target, arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

m = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))

for i in tmp:
    answer = bin(i, data, 0, len(data)-1)
    if answer != None:
        print(1)
    else:
        print(0)
