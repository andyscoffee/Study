# BOJ 1712
import math

a, b, c = map(int, input().split())
f = True
if b >= c:
    print(-1)
    f = False
while f:
    print(math.ceil((a+1)/(c-b)))
    break
