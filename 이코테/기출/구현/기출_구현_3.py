# 문자열 압축 (2020 카카오 신입 공채)

def solution(s):
    answer = 0
    result=[] # 쪼갠 문자열의 길이(1로 자른 문자열의 길이...)
    
    if len(s)==1: # 인풋 s가 1이면 1을 반환
        return 1 
    
    for i in range(1, (len(s)//2)+1): # 자를 수 있는 문자열의 최대 길이는 문자열 s의 절반
        b = '' # 잘라서 표현한 문자열 저장
        cnt = 1 # 문자열 반복 체크
        tmp=s[:i] # 문자열 반복 비교용으로 첫부분 저장
        
        for j in range(i, len(s), i): # i만큼 문자열을 계속 자름
            if tmp==s[j:i+j]: 
                cnt+=1 
            else: 
                if cnt!=1:
                    b = b + str(cnt)+tmp 
                else:
                    b = b + tmp 
                tmp=s[j:j+i] 
                cnt = 1 
        if cnt!=1:
            b = b + str(cnt) + tmp 
        else: 
            b = b + tmp 
        result.append(len(b))
    answer=min(result)
    return answer
