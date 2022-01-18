# 음양 더하기 (월간 코드 챌린지 시즌2)

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
            
    return answer
