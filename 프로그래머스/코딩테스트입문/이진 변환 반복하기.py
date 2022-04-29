# 월간 코드 챌린지 시즌 1 이진 변환 반복하기(난이도 2)

def solution(s):
    if s == "1":
        return [0, 0]

    answer = [1, 0]
    answer[1] += s.count("0")
    new_s = format(s.count("1"), "b")

    while (new_s) != "1":
        answer[1] += new_s.count("0")
        new_s = format(new_s.count("1"), "b")
        answer[0] += 1

    return answer


print(solution("110010101001"), [3, 8])
print(solution("01110"), [3, 3])
print(solution("1111111"), [4, 1])
