# 2018 KAKAO BLIND RECRUITMENT 다트 게임[1차]

import math


def solution(dartResult):
    answer = 0
    data = []
    tmp = ""
    for r in dartResult:
        if r.isnumeric():
            tmp += r
        elif r == "S":
            data.append(int(tmp))
            tmp = ""
        elif r == "D":
            data.append(int(pow(int(tmp), 2)))
            tmp = ""
        elif r == "T":
            data.append(int(pow(int(tmp), 3)))
            tmp = ""
        elif r == "*":
            if len(data) > 1:
                data[-2] *= 2
            data[-1] *= 2
        elif r == "#":
            data[-1] *= (-1)

    answer = sum(data)
    return answer


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D"))
print(solution("1D2S3T*"))
