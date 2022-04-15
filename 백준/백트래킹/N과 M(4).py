# 15652

import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
data = [i for i in range(1, n+1)]
tmp = list(combinations_with_replacement(data, m))
for i in tmp:
    for data in i:
        print(data, end=" ")
    print()
