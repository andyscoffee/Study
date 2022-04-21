# 11051

import sys

dp = [1]*1001
n, k = map(int, sys.stdin.readline().split())

for i in range(1, n+1):
    dp[i] = dp[i-1]*i

ans = dp[n]//(dp[k]*dp[n-k])
print(ans % 10007)
