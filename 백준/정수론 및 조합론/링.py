# 3036
from fractions import Fraction
import sys

n = int(sys.stdin.readline())
rings = list(map(int, sys.stdin.readline().split()))
for i in range(1, len(rings)):
    if rings[0] % rings[i] == 0:
        print(rings[0]//rings[i], end="")
        print("/1")
    else:
        print(Fraction(rings[0], rings[i]))
