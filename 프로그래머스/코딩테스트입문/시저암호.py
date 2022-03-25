def solution(s, n):
    answer = ""
    for i in s:
        tmp = ord(i) + n
        if tmp > 122:  # i가 소문자인 경우
            answer += chr(ord(i)+n-26)
            continue
        elif ord(i) < 91 and tmp > 90:  # i가 대문자인 경우
            answer += chr(ord(i)+n-26)
            continue
        elif i == " ":
            answer += " "
            continue
        answer += chr(ord(i)+n)

    return answer
