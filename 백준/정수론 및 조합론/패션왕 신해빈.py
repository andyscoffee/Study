# 9375
import sys


def solution(clothes):
    answer = 1
    dic = {}

    for i in range(len(clothes)):
        val, part = clothes[i]
        if part not in dic.keys():
            dic[part] = []
            dic[part].append(val)
        else:
            dic[part].append(val)

    for i in dic.keys():
        answer *= (len(dic[i])+1)

    return answer-1


tc = int(sys.stdin.readline().strip())
for t in range(tc):
    n = int(sys.stdin.readline().strip())
    clothes = []
    for i in range(n):
        item, where = sys.stdin.readline().split()
        clothes.append([item, where])
    print(solution(clothes))
