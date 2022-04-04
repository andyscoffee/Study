# BOJ 1978
import math


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


n = int(input())
cnt = 0
data = list(map(int, input().split()))
for i in data:
    if is_prime(i):
        cnt += 1
print(cnt)
