# 14889
from itertools import combinations
import sys

n = int(sys.stdin.readline().strip())
players = [i for i in range(n)]
data = [[0] for _ in range(n)]
ans = 1e9

for i in range(n):
    data[i] = list(map(int, sys.stdin.readline().split()))

team = list(combinations(players, n//2))
for t in team:
    teamA = 0
    teamB = 0
    for i in t:
        for j in t:
            teamA += data[i][j]
    team_2 = [i for i in range(n)if i not in t]
    for i in team_2:
        for j in team_2:
            teamB += data[i][j]
    if ans > abs(teamA-teamB):
        ans = abs(teamA-teamB)
print(ans)
