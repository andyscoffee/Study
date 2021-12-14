# 모험가 길드(핵심 유형)

n = int(input())
cnt = 0 # 그룹 수
tmp = 0 # 아직 떠나지 못한 모험가 수

fear = list(map(int, input().split()))

fear.sort()

for i in range(n):
  tmp += 1 # 모험가 1명 추가
  if tmp>=fear[i]: #  모험가의 수가 공포도보다 높다면
    cnt += 1
    tmp = 0 # 모험가 떠났기에 0으로 초기화

print(cnt)