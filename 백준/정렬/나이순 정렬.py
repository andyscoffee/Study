# 10814

import sys

n = int(sys.stdin.readline().strip())
data = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    data.append((age, name, i))
data.sort(key=lambda x: (int(x[0]), x[2]))

for a, n, i in data:
    print(a, n)
