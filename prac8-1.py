# 1로 만들기

n = int(input())
dp = [0] * 30001
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1  # 비교를 위한 값 설정(이전 최적해에 1을 더해준 연산 수행)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)  # 2,3,5로 나누는 연산 수행하기에 마지막 값에 연산 횟수 1을 더해줌
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)  # 2,3,5로 나누는 연산 수행하기에 마지막 값에 연산 횟수 1을 더해줌
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)  # 2,3,5로 나누는 연산 수행하기에 마지막 값에 연산 횟수 1을 더해줌

print(dp[n])
