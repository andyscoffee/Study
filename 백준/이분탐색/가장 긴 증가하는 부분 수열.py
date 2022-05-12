# 11053

# D[i]=arr[i]를 마지막 원소로 갖는 부분 수열의 최대 길이 모든 0<=j<i에 대하여 D[i] = max(D[i], D[j]+1), if arr[j]<arr[i]
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1]*n
for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
