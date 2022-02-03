def solution(id_list, report, k):
    answer = [0] * (len(id_list))
    n_rpt = set(report) # 레포트의 중복 제거
    dic = dict() # 신고당한 사람:신고당한 횟수
    check = dict() # k회 이상 신고당한 사람들
    cnt = dict() # 신고자: 정지 처리 결과 메일 발송 횟수

    for i in n_rpt:
        rpt, rptd = i.split()
        cnt[rpt] = 0 # 나중에 횟수 처리를 위해
        if rptd not in dic.keys(): # 새로운 신고라면 1 
            dic[rptd] = 1
        else: # 이미 신고당한 사람이면 횟수 1 추가
            dic[rptd] += 1

    for i in dic.keys():
        if dic[i] >= k: # 신고당한 횟수가 k회 이상이라면 저장
            check[i] = True 

    for i in n_rpt:
        rpt, rptd = i.split()
        if rptd in check.keys(): # k회 이상 신고당한 사람일 경우
            cnt[rpt] += 1 # 메일 발송 횟수 1 추가

    for i in range(len(id_list)):
        if id_list[i] in cnt.keys():
            answer[i] = cnt[id_list[i]]

    return answer
    
    
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
id_list = ["muzi", "frodo", "apeach", "neo"]
k = 2

print(solution(report, id_list, k))
