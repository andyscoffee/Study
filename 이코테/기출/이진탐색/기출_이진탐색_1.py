# 정렬된 배열에서 특정 수의 개수 구하기 (Zoho 인터뷰)

from bisect import bisect_left, bisect_right


def cnt_by_range(a, left, right):
    r = bisect_right(a, right)
    l = bisect_left(a, left)
    return r - l


n, x = map(int, input().split())
data = list(map(int, input().split()))
print(cnt_by_range(data, x, x))
