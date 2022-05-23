# 10814

import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    data.append((age, name, i))
data.sort(key=lambda x: (x[0], x[2]))

for a, n, i in data:
    print(a, n)
