# 14888 삼성 SW 역량 테스트 기출 문제 1

import sys

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())
max_res = -1e9
min_res = 1e9


def dfs(depth, num, add, sub, mul, div):

    global max_res, min_res
    if depth == n:
        max_res = max(max_res, num)
        min_res = min(min_res, num)
        return
    if add:
        dfs(depth+1, num+data[depth], add-1, sub, mul, div)
    if sub:
        dfs(depth+1, num-data[depth], add, sub-1, mul, div)
    if mul:
        dfs(depth+1, num*data[depth], add, sub, mul-1, div)
    if div:
        if num < 0:
            dfs(depth+1, -(abs(num)//data[depth]), add, sub, mul, div-1)
        else:
            dfs(depth+1, num//data[depth], add, sub, mul, div-1)


dfs(1, data[0], add, sub, mul, div)

print(max_res)
print(min_res)
