# 1764

import sys

n, m = map(int, sys.stdin.readline().split())
a = set()
ans = set()

for _ in range(n):
    a.add(sys.stdin.readline().rstrip())
for _ in range(m):
    tmp = sys.stdin.readline().rstrip()
    if tmp in a:
        ans.add(tmp)

print(len(ans))
for i in sorted(list(ans)):
    print(i)
