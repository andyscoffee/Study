# 4153

while True:
    a, b, c = map(int, input().split())
    num = []
    num.append(a)
    num.append(b)
    num.append(c)
    if sum(num) == 0:
        break
    num.sort()
    c = num.pop()  # 가장 큰 원소
    a = num[0]
    b = num[1]
    if (pow(a, 2)+pow(b, 2)) == pow(c, 2):
        print("right")
    else:
        print("wrong")
