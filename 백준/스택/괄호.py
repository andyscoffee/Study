# 9012

from collections import deque
import sys


def solution(s):
    st = deque()
    answer = True
    if s.count("(") != s.count(")"):
        return False
    for i in s:
        if s[0] == ")":
            return False
        st.append(i)
        if i == ")" and len(st) > 1:
            st.pop()
            st.pop()
    if len(st) != 0:
        return False

    return answer


n = int(sys.stdin.readline())

for _ in range(n):
    ps = sys.stdin.readline().strip()
    if solution(ps):
        print("YES")
    else:
        print("NO")
