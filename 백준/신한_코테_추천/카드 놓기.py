# 5568

import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
data = []
ans = set()

for i in range(n):
    data.append(int(sys.stdin.readline()))
tmp = list(permutations(data, k))

for i in tmp:
    ans.add("".join(list(map(str, i))))
print(ans)
