# 1021

import sys
from collections import deque

n, m = int(sys.stdin.readline().split())
needs = list(map(int, sys.stdin.readline().split()))
data = deque([i for i in range(1, n+1)])
