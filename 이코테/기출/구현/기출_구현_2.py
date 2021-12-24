# 문자열 재정렬(Facebook 인터뷰)

s = input()
alpha = []
num = []
for i in s:
    if i.isalpha() == True:
        alpha.append(i)
    elif i.isdigit() == True:
        num.append(i)

alpha.sort()
num.sort()

for i in alpha:
    print(i, end='')
for i in num:
    print(i, end='')
