# 1002
import math

tc = int(input())
for _ in range(tc):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))  # 두 원 사이의 거리
    if d == 0 and r1 == r2:  # 반지름이 같은 동심원일 경우
        print(-1)
    elif d == abs(r1-r2) or d == r1+r2:  # 내접이거나 외접인 경우
        print(1)
    elif abs(r1-r2) < d < (r1+r2):  # 서로 다른 두 점에서 만나는 경우
        print(2)
    else:
        print(0)
