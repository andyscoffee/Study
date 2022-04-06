# BOJ 10809

word = input()  # 단어
dic = dict()
s = set()  # 중복 체크용
for i in range(97, 123):  # 알파벳:나온 순서(-1로 초기화)
    dic[chr(i)] = -1

for i in range(len(word)):
    if word[i] not in s:
        dic[word[i]] = i
        s.add(word[i])

for i in dic.keys():
    print(dic[i], end=' ')
