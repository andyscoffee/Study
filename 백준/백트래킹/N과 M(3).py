# 15651

import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())
data = [i for i in range(1, n+1)]
tmp = list(product(data, repeat=m))
for i in tmp:
    for data in i:
        print(data, end=" ")
    print()
