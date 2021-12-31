# 고정점 찾기 (Amazon 인터뷰)

n = int(input())
data = list(map(int, input().split()))

def bin(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
res = bin(data, 0, len(data))
if res == None:
  print('-1')
else:
  print(res)