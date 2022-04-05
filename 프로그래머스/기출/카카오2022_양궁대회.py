# 2022 KAKAO BLIND RECRUITMENT

def solution(n, info):
    answer = [0]
    tmp = []
    shots = n
    pershot = dict()
    for shot in info:  # 인포 루프 돌면서 어피치 화살 수 +1 씩 저장
        tmp.append(shot + 1)

    for shot in range(len(info)):
        pershot[10-shot] = (10-shot)/tmp[shot]
    print("Per one shot: ", pershot)
    print("tmp: ", tmp)
    print()
    New_dict = sorted(pershot.items(), reverse=True, key=lambda x: x[1])
    print("NEW :", New_dict)
    return answer


"""
해쉬 테이블 만들어서 점수/화살수+1 밸류로 키값은 점수 
점수:화살한발당<- 저장 ex) 10:10 --> 한발에 10점짜리 (어피치는 0점임), 10 : 5 -> 2발을 쏴야 10점 획득 가능(즉 발당 5점짜리 화살)
해서 10:5 9:3 8:8 7:7 -> 이런 경우 한발에 8점, 7점인 화살을 먼저 소모(발당 얻을 수 있는 수익이 가장 높게)
"""

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]),
      [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0])
# print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), [-1])
"""print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]),
      [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0])
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]),
      [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2])"""
