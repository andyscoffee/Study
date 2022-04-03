# 부녀회장이 될테야 2775
t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    house = [[1]*14 for _ in range(k+1)]

    for i in range(14):
        house[0][i] = i+1
    for i in range(1, k+1):
        for j in range(1, n):
            house[i][j] = house[i-1][j] + house[i][j-1]

    print(house[k][n-1])
