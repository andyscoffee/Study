# 2609
import sys


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x*y)//gcd(x, y)


nums = list(map(int, sys.stdin.readline().split()))
nums.sort(reverse=True)
print(gcd(nums[0], nums[1]))
print(lcm(nums[0], nums[1]))
