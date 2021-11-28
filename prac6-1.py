# 위에서 아래로

n = int(input())
list = []
for i in range(n):
    list.append(int(input()))

list.sort(reverse=True)

for i in list:
    print(i, end=" ")
