# 숫자 카드 게임

n, m = map(int, input().split())
res = 0

for i in range(n):
    data = map(int, input().split())
    min_value = min(data)
    res = max(res, min_value)
print(res)
