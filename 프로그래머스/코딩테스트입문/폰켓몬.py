# 폰켓몬 (찾아라 프로그래밍 마에스터)
def solution(nums):
    answer = 0
    n_nums = set(nums)
    for i in range(len(nums)):
        if answer >=len(nums)//2:
            break
        if answer >= len(n_nums):
            break
        answer += 1
    return answer
