# 큰 수의 법칙(2019 국가 교육 기관 코딩테스트)

n, m, k = map(int, input().split())  # 배열의 크기, 덧셈 횟수, 연속으로 더할 수 있는 최대 횟수
group = list(map(int, input().split()))
sum = 0
cnt = 0

group.sort()
first = group[n - 1]
second = group[n - 2]

cnt = int(m / (k + 1)) * k
cnt = cnt + m % (k + 1)
sum = cnt * first
sum = sum + (m - cnt) * second

print(sum)
