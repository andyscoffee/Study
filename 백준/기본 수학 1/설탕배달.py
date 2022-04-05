
# 설탕 배달 (DP) 처음
n = int(input())
sugar = [-1]*5001
sugar[0] = 0
sugar[3], sugar[5] = 1, 1
for i in range(6, n+1):
    if i % 5 == 0:
        sugar[i] = sugar[i-5]+1
    elif i % 3 == 0:
        sugar[i-3] = sugar[i-3] + 1
    elif sugar[i-5] > 0 and sugar[i-3] > 0:
        sugar[i] = min(sugar[i-3], sugar[i-5]+1)
# DP2
n = int(input())
arr = [5001] * (5001)
arr[3], arr[5] = 1, 1

for i in range(6, n+1):
    arr[i] = min(arr[i-3], arr[i-5]) + 1

if arr[n] < 5001:
    print(arr[n])
else:
    print(-1)

# 설탕 배달 그리디 (5(더 큰수)로 나누는게 횟수가 더 빠르게 줄기에 3씩 빼다 5로 나누어떨어지면 종료)
n = int(input())
cnt = 0
while n >= 0:
    if n % 5 == 0:
        cnt += n//5
        print(cnt)
        break
    n -= 3
    cnt += 1
else:
    print(-1)
