# 1593

import sys

n, m = map(int, sys.stdin.readline().split())
target = sys.stdin.readline().rstrip()
full = sys.stdin.readline().rstrip()

t_cnt = [0] * 52  # 대소문자 개수만큼 리스트, 인덱스에 각 글자가 나온 개수 저장
f_cnt = [0] * 52
ans = 0

for t in target:
    if 'a' <= t <= 'z':
        t_cnt[ord(t)-ord('a')] += 1
    else:
        t_cnt[ord(t)-ord('A')+26] += 1

start, length = 0, 0

for w in full:
    if 'a' <= w <= 'z':
        f_cnt[ord(w)-ord('a')] += 1
    else:
        f_cnt[ord(w)-ord('A')+26] += 1

    length += 1

    if length == len(target):
        if t_cnt == f_cnt:
            ans += 1

        if 'a' <= full[start] <= 'z':
            f_cnt[ord(full[start])-ord('a')] -= 1
        else:
            f_cnt[ord(full[start])-ord('A')+26] -= 1

        start += 1
        length -= 1

print(ans)
