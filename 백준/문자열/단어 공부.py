# BOJ 1157

word = input()
cnt = dict()
for l in word:
    if l.upper() in cnt.keys():
        cnt[l.upper()] += 1
    else:
        cnt[l.upper()] = 1
tmp = -1
for i in cnt.keys():
    if cnt[i] == max(cnt.values()):
        tmp += 1
if tmp > 0:
    print("?")
else:
    for i in cnt.keys():
        if cnt[i] == max(cnt.values()):
            print(i)
