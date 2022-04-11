# 3009
from collections import Counter
w = []
h = []
n1, n2 = 0, 0
for _ in range(3):
    a, b = map(int, input().split())
    w.append(a)
    h.append(b)

for i, j in zip(w, h):
    if Counter(w)[i] == 1:
        n1 = i
    elif Counter(h)[j] == 1:
        n2 = j
print(n1, n2)
