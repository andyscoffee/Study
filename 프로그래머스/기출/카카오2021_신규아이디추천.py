# 신규 아이디 추천(카카오 2021 블라인드 채용)
def solution(new_id):
    new_id = new_id.lower() # 1단계
    answer = ''

    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word # 2단계

    while '..' in answer:
        answer = answer.replace('..', '.') # 3단계
        
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1] # 4단꼐

    if answer == '':
        answer = 'a' # 5단계

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.': 
            answer = answer[:-1] # 6단계

    while len(answer) <= 2:
        answer += answer[-1]
        if len(answer) == 3:
            break # 7단계
    return answer
