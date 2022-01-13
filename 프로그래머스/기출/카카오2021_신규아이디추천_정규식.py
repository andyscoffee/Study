import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    """7단계 해설 - 1. 문자열 길이가 2 초과면 그대로 반환. 
    아니라면(길이가 2이하) 원하는 길이(3)를 맞추기 위해 3에서 본래길이(len(st))를 빼준 개수만큼 for문을 돌리면서 맨마지막 글자를 리스트로 넣은 후 join으로 합쳐 st에 더해줌.
    7단계는 for, join 말고 st + st[-1] * (3-len(st)) 이렇게도 가능
    """
    return st
