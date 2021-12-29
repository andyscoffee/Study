# 실패율  (2019 카카오 신입공채 1차)

def solution(N, stages):
    dict = {}
    num = len(stages)
    for i in range(1, N+1):
        if num == 0:
            dict[i] = 0
        else:
            cnt = stages.count(i)
            dict[i] = cnt/num
            num -= cnt
    return sorted(dict, key = lambda x: dict[x], reverse = True)
