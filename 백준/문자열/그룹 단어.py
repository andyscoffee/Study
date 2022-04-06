# BOJ 1316

n = int(input())
ans = n
for i in range(n):
    s = input()
    dic = dict()
    for i in range(len(s)):
        if s[i] in dic.keys():
            dic[s[i]].append(i)
        else:
            dic[s[i]] = []
            dic[s[i]].append(i)
    for i in dic.keys():
        if len(dic[i]) == 1:
            continue
        # 알파벳이 연속한다면 마지막 인덱스-첫 인덱스가 나온횟수-1이 되어야 함
        elif dic[i][-1]-dic[i][0] != len(dic[i])-1:
            ans -= 1
            break
print(ans)
