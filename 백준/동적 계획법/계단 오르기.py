# 2579

import sys
N = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(N)]
dp = [0 for _ in range(N)]
if N > 2:
    dp[0] = data[0]
    dp[1] = data[0]+data[1]
    dp[2] = max(data[0]+data[2], data[1]+data[2])
    for i in range(3, N):
        dp[i] = (max(dp[i-2], dp[i-3]+data[i-1])+data[i])

    print(dp[N-1])
else:
    print(sum(data))
