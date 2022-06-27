# 10968

import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

prepix = [0]*m
p_sum, ans = 0, 0
prepix[0] = 1

for i in range(n):
    p_sum += data[i]  # 부분합 저장
    prepix[p_sum % m] += 1  # 나머지가 같은 두 부분합 구간 -> m의 배수

for i in prepix:
    ans += i*(i-1)//2  # 나머지가 0인 경우, 부분합 자체가 m의 배수기에 index가 0인 것을 포함

print(ans)
