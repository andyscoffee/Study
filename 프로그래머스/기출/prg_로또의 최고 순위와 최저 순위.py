def rank(num):
    if num == 6:
        res = 1
    elif num == 5:
        res = 2
    elif num == 4:
        res = 3
    elif num == 3:
        res = 4
    elif num == 2:
        res = 5
    else:
        res = 6
    return res


def solution(lottos, win_nums):
    answer = []
    tmp = lottos.count(0)  # 0의 갯수
    lose = 0  # 최소 등수 체크
    for i in lottos:
        for j in win_nums:
            if i == j:
                lose += 1  # 당첨 숫자 갯수 = 최소 등수
    win = lose + tmp  # 0의 갯수 + 당첨 숫자 갯수 = 최대 등수

    answer.append(rank(win))
    answer.append(rank(lose))
    return answer
