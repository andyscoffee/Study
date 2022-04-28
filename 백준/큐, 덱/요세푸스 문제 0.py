# 11866

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
data = deque([i for i in range(1, n+1)])
tmp = 1
ans = []

while data:
    if tmp == k:  # k번째 수일때 정답 배열로 빼냄
        ans.append(data.popleft())
        tmp = 1
    else:  # 아닐때는 다시 맨 뒤로 돌림
        data.append(data.popleft())
        tmp += 1

print("<", end='')
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end=">")
    else:
        print(ans[i], end=", ")
