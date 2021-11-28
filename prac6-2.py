# 성적이 낮은 순서로 학생 출력하기

n = int(input())
list = []
for i in range(n):
    data = input().split()
    list.append((data[0], int(data[1])))
list.sort(key=lambda x: x[1])

for x in list:
    print(x[0], end=" ")
