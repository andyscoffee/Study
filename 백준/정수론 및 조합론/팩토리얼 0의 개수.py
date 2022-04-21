# 1676

import sys
n = int(sys.stdin.readline())
dp = [1]*501
cnt = 0

for i in range(1, n+1):
    dp[i] = dp[i-1]*i
tmp = str(dp[n])
for i in range(len(tmp), 0, -1):
    if tmp[i-1] == "0":
        cnt += 1
    else:
        break
print(cnt)
