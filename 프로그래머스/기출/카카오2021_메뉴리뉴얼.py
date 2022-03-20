# 2021 KAKAO BLIND RECRUITMENT
from itertools import combinations


def solution(orders, course):
    answer = []
    comdict = {}  # 메뉴 조합:주문 횟수
    coursedict = {}  # (정해진) 코스의 메뉴 수 : 최대 주문 횟수

    for num in course:
        for i in orders:
            i = sorted(list(i))
            tmp = list(combinations(i, num))
            tmp.sort()
            for t in tmp:
                if t not in comdict:
                    comdict[t] = 1
                else:
                    comdict[t] += 1

    for num in course:
        coursedict[num] = 0
        for key in comdict:
            if comdict[key] >= 2 and len(key) == num:
                if comdict[key] > coursedict[num]:
                    coursedict[num] = comdict[key]

    for n in course:
        for key in comdict:
            # 코스에 정해진 메뉴 수의 조합이고 최대 주문횟수와 같다면 삽입
            if len(key) == n and comdict[key] == coursedict[n]:
                answer.append("".join(key))
    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
      [2, 3, 4]), ["AC", "ACDE", "BCFG", "CDE"])
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [
      2, 3, 5]), ["ACD", "AD", "ADE", "CD", "XYZ"])
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]), ["WX", "XY"])
