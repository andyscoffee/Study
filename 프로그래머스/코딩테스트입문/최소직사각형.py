# 위클리 챌린지 최소 직사각형 (난이도 1)
def solution(sizes):
    answer = 0
    width = []
    length = []
    for i in sizes:
        width.append(max(i))
        length.append(min(i))
    answer = max(width)*max(length)
    return answer
