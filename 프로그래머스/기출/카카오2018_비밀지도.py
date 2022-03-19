# 2018 KAKAO BLIND RECRUITMENT 비밀 지도(난이도 1)

def solution(n, arr1, arr2):
    answer = []
    listb1 = []
    listb2 = []

    for i in arr1:  # arr1을 이진수 형식으로 저장
        b = format(i, 'b')
        if len(b) != n:
            while len(b) != n:
                b = '0'+b
        listb1.append(b)
    for i in arr2:  # arr2를 이진수 형식으로 저장
        b2 = format(i, 'b')
        if len(b2) != n:
            while len(b2) != n:
                b2 = '0'+b2
        listb2.append(b2)

    for a, b in zip(listb1, listb2):  # arr1, arr2에서 하나씩 꺼냄
        tmp = ''
        for i, j in zip(a, b):  # 꺼낸 한줄에서 str 하나씩 검사
            if i == '1' or j == '1':  # 둘 중 하나가 1이라면 #, 아니라면 공백 삽입
                tmp += '#'
            else:
                tmp += " "
        answer.append(tmp)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]),
      ["#####", "# # #", "### #", "# ##", "#####"])
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]),
      ["######", "### #", "## ##", " #### ", " #####", "### # "])
