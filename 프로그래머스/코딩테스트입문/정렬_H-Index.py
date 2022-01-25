"""
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 
나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

h = 1, 5편 중 1번 이상 인용된 논문 4개(6,5,3,1) h_cnt  = 4
나머지 논문(0,1) 0번, 1번 <=1 인용 
citations[h_cnt] <- h이하 중 제일 많이 인용 안한 논문 = 0 <= h(=1) -> h = 1

h = 2, 5편 중 2번 이상 인용된 논문 3개(6,5,3) h_cnt = 3
나머지 논문(0,1) 0번, 1번 <=2 인용
citations[h_cnt] = 1 <= h(=2) -> h = 2

h = 3, 5편 중 3번 이상 인용된 논문 3개 (6,5,3) h_cnt = 3
나머지 논문 (0,1) 0번, 1번 <3 인용 -
citations[h_cnt] = 1 <=h(3) -> h = 3

h = 4, 5편 중 4번 이상 인용된 논문 2개 (4>2) h_cnt < h -> break 
"""


def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for h in range(1, len(citations) + 1):
        h_cnt = 0  # 인용 횟수
        for n in citations:
            if n >= h:
                h_cnt += 1
            # 역순으로 정렬 했을 때 n이 h보다 작은 경우, 다음 논문또한 i보다 작음
            # 더 이상 h_cnt가 늘어나지 않기에 브레이크
            else:
                break
        # 인용 횟수가 h보다 크고 
        if h_cnt >= h:
            # 인용 횟수가 h보다 큰 논문이 전체 논문의 수와 같다면
            if h_cnt == len(citations):
                answer = h
            # h보다 적게 인용된 논문 중 가장 많이 인용된 논문이 h회 이하 인용이라면
            elif citations[h_cnt] <= h:
                answer = h
        else:
            break
    return answer


answers = [9,9,9,12]  # [4,3,1,1,1]답은 3
print(solution(answers))
