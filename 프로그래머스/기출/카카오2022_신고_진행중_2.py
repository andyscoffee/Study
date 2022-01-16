report = ["ryan con", "ryan con", "ryan con", "ryan con"]
id_list = ["con", "ryan"]
k = 3
# 까지 입력 조건
check_list = []  # 제재가 확정된 사람을 저장할 배열
answer = [0] * (len(id_list))

dic = {}
rp_num = {}  # id별 신고당한 횟수 저장용 사전

for i in id_list:
    dic[i] = []  # 신고자 : [신고당한목록] 사전 생성을 위한 key: 빈 리스트 생성
    rp_num[i] = 0

for i in range(len(report)):
    singo, hogu = report[i].split()  # 분리
    if hogu not in dic[singo]:  # 중복신고가 아니라면
        dic[singo].append(hogu)  #사전에 삽입

for id in range(len(id_list)):  # 유저 목록만큼 반복
    for data in list(dic.values()): # 중복을 제거한 레포트를 순회하면서
        if id_list[id] in data: 
            rp_num[id_list[id]] += 1 # 유저별 신고당한 횟수 체크
            if rp_num[id_list[id]] >= k: # 신고당한 횟수가 k회를 넘어가는 경우
                check_list.append(id_list[id]) # 확정 리스트에 삽입

for reported in check_list:  
    for j in range(len(id_list)): 
        if reported in list(dic.values())[j]: 
            answer[j] += 1

print(answer)
