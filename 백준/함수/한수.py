# 1065 한수

arr = [False]*(1001)
for i in range(1, 1001):
    if i <= 99:
        arr[i] = True  # 두자릿수까지는 전부 등차수열
    elif i <= 999:
        tmp = str(i)
        if int(tmp[0])-int(tmp[1]) == int(tmp[1])-int(tmp[2]):
            arr[i] = True
n = int(input())
cnt = 0
for i in range(n+1):
    if arr[i]:
        cnt += 1
print(cnt)
