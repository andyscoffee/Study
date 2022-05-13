# 11478

import sys

s = sys.stdin.readline().rstrip()
ans = set()
cnt = 1
while cnt < len(s):
    for i in range(len(s)):
        ans.add(s[i:i+cnt])
    cnt += 1
print(len(ans)+1)  # 전체 문자열 1개 더하기
