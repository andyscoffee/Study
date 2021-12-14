#만들 수 없는 금액(K 대회 기출)

n = int(input())
coins = list(map(int, input().split()))
coins.sort()
tmp = 1

for i in coins:
  if tmp < i:
    break
  tmp += i

print(tmp)