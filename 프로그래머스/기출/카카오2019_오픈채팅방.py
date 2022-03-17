# 2019 KAKAO BLIND RECRUITMENT
def solution(record):
    answer = []
    tmp = []
    data = {}
    for rec in record:
        r = rec.split()
        if r[0] == "Enter":
            data[r[1]] = r[2]
            tmp.append(r[1] + " 들어왔습니다.")  # 2분할을 위해 들어왔습니다/나갔습니다만 저장
        elif r[0] == "Change":
            data[r[1]] = r[2]
        else:
            tmp.append(r[1] + " 나갔습니다.")  # 2분할을 위해 들어왔습니다/나갔습니다만 저장
    for t in tmp:
        tmpo = t. split()  # uid / 들어or나갔
        if tmpo[0] in data.keys():
            # uid를 사전(data)에 저장해둔 이름으로 변경, 포맷에 맞게 저장
            answer.append(data[tmpo[0]]+"님이 "+tmpo[1])

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.",
          "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
print(solution(record))
