# 신고 결과 받기 (2022 KAKAO BLIND RECRUITMENT)
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi","muzi frodo", "muzi frodo", "apeach frodo"]
id_list = ["muzi", "frodo", "apeach", "neo"]
k = 2
# 까지 입력 조건
check_list = [0]*(len(id_list))
answer = [0]*(len(id_list))
dic = {}
rp_num = {} # id별 신고당한 횟수 저장용 사전

for i in id_list:
  dic[i] = [] # 신고자 : [신고당한목록] 사전 생성을 위한 key: 빈 리스트 생성
  rp_num[i] = 0

for i in range(len(report)):
  singo, hogu = report[i].split() # 분리
  if hogu not in dic[singo]: # 중복신고가 아니라면
    dic[singo].append(hogu) #사전에 삽입

"""   
print('dic : ', dic)
print('rp_num: ', rp_num)
print(list(dic.values())[0])
for i in list(dic.values()):
  print(i)"""
i = 0
for id in id_list:
  for data in list(dic.values()):
    if id in data:
      rp_num[id] += 1 # 유저별 신고당한 횟수 체크
      if rp_num[id] >=k:
        check_list[i] += 1
        
  i += 1
#위의 억지코드 i 관련 내용은 맞지만 깔끔하게 i 제거하는 수정 필요    
"""
print('rp_num: ', rp_num)
for r_num in rp_num.values():
  print(r_num)
  if r_num >= k:
    answer[r_num] += 1
print(answer)"""


print('중복 제거한 레포트 : ', dic)
print('신고 당한 횟수: ', rp_num)
print("신고 유효면 1, 아니면 0:", check_list)
"""프로도(체크리스트1)랑 네오(체크리스트3)를 신고한 사람 -> 무지, 무지, 프로도, 어피치
은 카운터 하나씩 쌓아서 앤서에 저장 -> [2,1,1,0]
루프 len(id_list)회, 0일떄 무효, 1이네? i는 1이네? id[i]는 프로도네?
프로도 신고한 사람은 누구지? 레포트 사전 밸류 돌면서 프로도 있는 사람 앤서자리에 1씩 더하기"""
#for i in range(len(id_list)):
#  if check_list[i] != 0:
"""
i = 0
for id in id_list:
  for data in list(dic.values()):
    if check_list[i] == 1: # i =1,3일때 걸림
      id_list[i]
"""

for i in range(len(dic.values())):
  if id_list[1] in list(dic.values())[i]:
    print(list(dic.keys())[i], 'id_list[1] 신고함')

