# 1874

import sys

n = int(sys.stdin.readline())
st = []
ans = []
cnt = 1
flag = True
for _ in range(n):
    num = int(sys.stdin.readline())
    while cnt <= num:
        st.append(cnt)
        ans.append("+")
        cnt += 1
    if st[-1] == num:
        st.pop()
        ans.append("-")
    else:
        flag = False
if flag:
    for i in ans:
        print(i)
else:
    print("NO")
