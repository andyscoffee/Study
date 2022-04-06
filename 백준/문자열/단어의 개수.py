# BOJ 1152

import sys

s = sys.stdin.readline().strip()
cnt = 0
for l in s:
    if l == " ":
        cnt += 1

if s == "":
    print(0)
else:
    print(cnt+1)
