# 4949

import sys

while True:
    line = sys.stdin.readline().rstrip()
    flag = True
    if line == ".":
        break
    data = []
    for l in line:
        if l == "[" or l == "(":
            data.append(l)

        elif l == "]":
            if data and data[-1] == "[":
                data.pop()
            elif not data or data[-1] != "[":
                flag = False
                break

        elif l == ")":
            if data and data[-1] == "(":
                data.pop()
            elif not data or data[-1] != "(":
                flag = False
                break
    if data:
        flag = False

    if flag:
        print("yes")
    else:
        print("no")
