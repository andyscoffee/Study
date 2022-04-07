# 2798 블랙 잭

from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))
ans = 0
flag = True
num = list(combinations(card, 3))

for i in num:
    if sum(i) == m:
        print(sum(i))
        flag = False
        break
    elif sum(i) < m:
        ans = max(ans, sum(i))
if flag:
    print(ans)
