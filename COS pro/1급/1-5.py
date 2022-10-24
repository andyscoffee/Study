def solution(n):
    # Write code here.
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 4  # 1+3
    for i in range(3, n+1):
        dp[n] = 1 + (2*n-1) + dp[n-2] + 4*(n-1)*(n-2)
# 1 + 2*n-1(우측 대각) + 2단계 이전 대각의 합 + 대각의 합에서 늘어난 수(같은 패턴에서 4*(n-1)씩 늘어난 수를 대각선(n-2)개 더 추가)
    return dp[n]


# The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

n2 = 2
ret2 = solution(n2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")
