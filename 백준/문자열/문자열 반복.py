#  BOJ 2675

t = int(input())
for i in range(t):
    ans = ""
    cnt, word = input().split()
    for i in range(len(word)):
        ans += word[i]*int(cnt)
    print(ans)
