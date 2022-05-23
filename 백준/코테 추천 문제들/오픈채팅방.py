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
            tmpo[0] = data[tmpo[0]]  # uid를 사전(data)에 저장해둔 이름으로 변경
            answer.append(tmpo[0]+"님이 "+tmpo[1])  # 포맷에 맞게 저장

    return answer
