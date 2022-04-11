# 2108

from collections import Counter
import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()
cnt = Counter(data).most_common()

print(round(sum(data)/n))
print(data[n//2])
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(data[-1]-data[0])
