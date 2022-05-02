# 14889
from itertools import combinations
import sys

n = int(sys.stdin.readline().strip())
player = [i for i in range(1, n+1)]
print(player)
data = []
min_sub = 1e9

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

tmp = list(combinations(player, n//2))
for t in tmp:
    teamA = list(t)
    teamB = [x for x in data if x not in t]
    print("A: ", teamA)
    print("B: ", teamB)
