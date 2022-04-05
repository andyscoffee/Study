# BOJ 9020
import math


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


t = int(input())

for i in range(t):
    tmp = int(input())
    if is_prime(tmp//2):
        print(tmp//2, tmp//2)
    else:
        for i in range(tmp//2, tmp):
            if is_prime(i) and is_prime(tmp-i):
                print(tmp-i, i)
                break
