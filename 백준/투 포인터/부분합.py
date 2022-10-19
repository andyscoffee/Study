# 1806

import sys

n, s = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
end, tmp = 0, 0
ans = n+1  # 길이의 최대값
for start in range(n):
    while tmp < s and end < n:
        tmp += data[end]
        end += 1
    if tmp >= s:
        ans = min(ans, (end-start))  # 가장 짧은 길이 선택
    tmp -= data[start]
if ans == (n+1):
    print(0)
else:
    print(ans)
