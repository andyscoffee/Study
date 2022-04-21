# 2981
import sys
from math import sqrt
"""
어떠한 숫자를 m으로 나누었을 때 나머지가 r이라면 해당 숫자는 아래와 같이 표기할 수 있습니다.
v[i] = m * temp[i] + r
따라서, 나머지 r을 지워주기 위해서는 같은 나머지를 같는 숫자를 빼주면 되는데 이는 아래와 같이 표기할 수 있습니다.
v[i] - v[i - 1] = m * (temp[i] - temp[i-1]) + (r - r)
따라서, N개의 숫자를 입력받고 오름차순으로 정렬해준 뒤 
(v[i] - v[i-1])의 최대공약수를 구한 뒤, 최대공약수의 약수를 오름차순으로 나열하면 되는 문제였습니다.
출처: https://jaimemin.tistory.com/1251 [꾸준함]
"""


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


n = int(sys.stdin.readline())
data = []  # 숫자 받을 리스트
gap = []  # 숫자간 차이 저장할 리스트
ans = []  # 정답을 담을 리스트
for _ in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()

for i in range(1, n):
    gap.append(data[i]-data[i-1])
tmp = gap[0]

for i in range(1, len(gap)):
    tmp = gcd(tmp, gap[i])

for i in range(2, int(sqrt(tmp))+1):
    if tmp % i == 0:
        ans.append(i)
        ans.append(tmp//i)

ans.append(tmp)
ans = list(set(ans))
ans.sort()
print(*ans)
