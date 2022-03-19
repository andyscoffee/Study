# 2021 KAKAO BLIND RECRUITMENT
from itertools import combinations


def solution(orders, course):
    answer = []
    comdict = {}
    """for i in orders:
        tmp = list(combinations(i, 2))
        for t in tmp:
            if t not in comdict:
                comdict[t] = 1
            else:
                comdict[t] += 1"""
    for num in course:
        for i in orders:
            tmp = list(combinations(i, num))
            tmp.sort()
            for t in tmp:
                if t not in comdict:
                    comdict[t] = 1
                else:
                    comdict[t] += 1
    print(comdict)  # dict[2] = [((A,C),4),(C,F),2),....]? <- 만들수는 있는데 좀

    # top2 = max(comdict.keys(), key=lambda x: comdict[x])
    for key in comdict:
        if comdict[key] >= 2 and len(key) == 2:
            print(key)

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
      [2, 3, 4]), ["AC", "ACDE", "BCFG", "CDE"])
"""print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [
      2, 3, 5]), ["ACD", "AD", "ADE", "CD", "XYZ"])
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]), ["WX", "XY"])
"""
