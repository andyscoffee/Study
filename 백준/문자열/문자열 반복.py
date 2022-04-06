<<<<<<< HEAD
# BOJ 2675
=======
#  BOJ 2675
>>>>>>> efe3991a31190020927783ba0a8db5be2a872d94

t = int(input())
for i in range(t):
    ans = ""
    cnt, word = input().split()
    for i in range(len(word)):
        ans += word[i]*int(cnt)
    print(ans)
