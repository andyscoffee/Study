# 떡 자르기


def cutter(array, target, start, end):
    res = 0

    while start <= end:
        total = 0
        mid = (start + end) // 2

        for i in array:
            if i > mid:  # 떡이 칼보다 더 긴 경우에만 자름(total에 더해줌)
                total += i - mid
        if total == target:
            return mid
        elif total < target:
            end = mid - 1
        else:
            start = mid + 1
            res = mid
    return res


n, m = map(int, input().split())
lineup = list(map(int, input().split()))

print(cutter(lineup, m, 0, max(lineup)))
