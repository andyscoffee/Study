# 1932

import sys

n = int(sys.stdin.readline())
dp = []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    dp.append(tmp)
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            left = 0
        else:
            left = dp[i-1][j-1]
        if j == i:
            right = 0
        else:
            right = dp[i-1][j]
        dp[i][j] = dp[i][j] + max(left, right)
print(max(dp[n-1]))
