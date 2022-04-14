# 2750 수 정렬하기 (삽입 정렬)
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
for i in range(1, len(data)):
    for j in range(i, 0, -1):
        if data[j] < data[j-1]:
            data[j], data[j-1] = data[j-1], data[j]
        else:
            break
for i in data:
    print(i)
