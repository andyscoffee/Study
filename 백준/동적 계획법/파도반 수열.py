# 9461 파도반 수열

import sys

dp = [0]*(101)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5
# 9 10   11  12   13   14
# 7 7+2 9+3 12+4 16+5 21+7
for i in range(9, 101):
    dp[i] = dp[i-1]+dp[i-5]

tc = int(sys.stdin.readline())
for i in range(tc):
    N = int(sys.stdin.readline())
    print(dp[N])
