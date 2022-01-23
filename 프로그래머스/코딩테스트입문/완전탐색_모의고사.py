def solution(answers):
    answer = []
    sp1 = [1,2,3,4,5]
    sp2 = [2,1,2,3,2,4,2,5]
    sp3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]

    for i in range(len(answers)):
        if sp1[i%5] == answers[i]:
            score[0] += 1
        if sp2[i%8] == answers[i]:
            score[1] += 1
        if sp3[i%10] == answers[i]:
            score[2] += 1
    print(score)
    top = max(score)
    for i in range(len(score)):
        if score[i] == top:
            answer.append(i+1)
    
    return answer
