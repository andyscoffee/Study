# 14888 삼성 SW 역량 테스트 기출 문제 1

import sys
from itertools import permutations
from collections import deque

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
oper = ["+", "-", "*", "//"]
oper_cnt = list(map(int, sys.stdin.readline().split()))
operator = []
for i in range(4):
    if oper_cnt[i] == 0:
        continue
    else:
        for j in range(oper_cnt[i]):
            operator.append(oper[i])
case = list(permutations(operator, len(operator)))
q = deque(case)
max_res = - 1e9
min_res = 1e9

while q:
    now = q.popleft()
    res = data[0]
    for i in range(1, len(data)):
        if now[i-1] == "+":
            res += data[i]
        elif now[i-1] == "-":
            res -= data[i]
        elif now[i-1] == "*":
            res *= data[i]
        else:
            if res < 0:
                res = -(abs(res)//data[i])
            else:
                res //= data[i]
    max_res = max(max_res, res)
    min_res = min(min_res, res)

print(max_res)
print(min_res)
