# 9372

import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
    print(n-1)  # MST로 모두 연결되어 있다면 간선의 개수는 n-1개
