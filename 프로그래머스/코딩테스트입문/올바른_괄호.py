# 올바른 괄호 (난이도 2)
from collections import deque


def solution(s):
    st = deque()
    answer = True

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


print(solution("()))"), "false")
print(solution("()()"), "true")
print(solution("(())()"), "true")
print(solution(")()("), "false")
print(solution("(()("), "false")
