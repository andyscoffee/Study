# 곱하기 혹은 더하기 (Facebook 인터뷰)

n = input()
res = int(n[0]) # 첫번째 숫자 처리

for i in range(1, len(n)):
  if int(n[i]) <=1 or res <= 1: 
    # 첫번째 숫자가 0 혹은 1이거나 현재 처리 숫자가 0 혹은 1이면 더하기
    res += int(n[i])
  else: # 그 외에는 곱하는게 숫자가 더 커짐
    res *= int(n[i])

print(res)