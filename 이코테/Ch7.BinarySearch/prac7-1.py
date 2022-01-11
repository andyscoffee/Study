# 부품 찾기


def bin(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
flist = list(map(int, input().split()))
m = int(input())
slist = list(map(int, input().split()))

flist.sort()

for i in slist:
    if bin(flist, i, 0, n - 1) == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
