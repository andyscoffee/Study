# 안테나 (2019 SW 마에스트로 입학 테스트))

n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1)//2])
