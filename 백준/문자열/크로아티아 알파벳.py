# BOJ 2941

import sys

cro = {"c=": 1, "c-": 1, "dz=": 2, "d-": 1, "lj": 1, "nj": 1, "s=": 1, "z=": 1}
s = sys.stdin.readline().strip()
l = len(s)
for i in range(len(s)-1):
    if s[i] == "c" and not s[i+1].isalpha():
        l -= 1
    elif s[i] == "d" and not s[i+1].isalpha():
        l -= 1
    elif s[i] == "s" and not s[i+1].isalpha():
        l -= 1
    elif s[i:i+3] == "dz=":
        l -= 2
    elif s[i] == "z" and not s[i+1].isalpha() and not s[i-1] == "d":
        l -= 1
    elif s[i] == "l" and s[i+1] == "j":
        l -= 1
    elif s[i] == "n" and s[i+1] == "j":
        l -= 1
print(l)
