# 거스름돈

n = int(input("거슬러 줘야할 돈을 입력하세요"))
coins = [500, 100, 50, 10]  # 거스름돈의 종류
cnt = 0  # 거스름돈의 갯수

for x in coins:
    cnt = cnt + n // x
    n = n % x

print(str(cnt) + " 개의 동전이 필요합니다")
