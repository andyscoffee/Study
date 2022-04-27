# 17298

import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
st = [0]
ans = [-1]*n
for i in range(1, n):
    while st:
        if data[st[-1]] < data[i]:
            ans[st.pop()] = data[i]
        else:
            break
    st.append(i)
print(*ans)
