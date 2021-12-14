s = input()
cnt1 = 0 # 전부 1로 바꾸는데 걸리는 횟수
cnt0 = 0 # 전부 0으로

if s[0] == '0':
    cnt1 += 1
else:
    cnt0 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]: # 다음 수가 다르고
        if s[i + 1] == '0': # 다음 수가 0이라면 1로 바꾸는 횟수 증가 
            cnt1 += 1
        else: # 반대 경우
            cnt0 += 1

print(min(cnt0, cnt1))