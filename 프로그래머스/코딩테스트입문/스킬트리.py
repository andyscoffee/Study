from collections import deque


def solution(skill, skill_trees):
    fail = 0
    for st in skill_trees:
        order = deque(skill)  # 한 스킬 트리당 한번씩 사용해야 하기에
        for ea in st:  # 스킬트리별 한 스킬마다
            if ea in order:  # 순서가 정해진 스킬이라면
                if order[0] == ea:  # 순서에 맞는지
                    order.popleft()  # 맞다면 다음 스킬 개방
                else:  # 선행스킬이 필요한 스킬임에도 선행스킬이 없다면 실패 1 증가
                    fail += 1
                    break
    answer = len(skill_trees)-fail
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]), 2)
