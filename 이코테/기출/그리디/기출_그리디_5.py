# 볼링공 고르기 (2019 SW 마에스트로 입학 테스트)

from itertools import combinations 
# 구하는 수 = 중복이 없는 순열에서 볼링공의 무게가 같지 않은 경우이기에 조합 사용 

n, m = map(int, input().split())
data = list(map(int, input().split()))

res = list(combinations(data, 2)) # nC2 계산(A, B 두 사람이기에)
cnt = len(res) # 조합 결과의 가짓수

for i in res:
  if i[0] == i[1]: 
    cnt -= 1 # nC2의 조합에서 두 볼링공의 무게가 같은 경우는 제외
print(cnt)