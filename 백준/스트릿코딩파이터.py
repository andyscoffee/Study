score = []


a, b, c = map(int, input().split())
n = int(input())
score.append(a)
score.append(b)
score.append(c)
each = [0]*n

for num in range(n):
    for i in range(3):
        i, j, k = map(int, input().split())
        each[num] += i*a + j*b + k*c
print(max(each))
