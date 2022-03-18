# Summer/Winter Coding(2019) 멀쩡한 사각형
def solution(w, h):
    answer = 0
    tmp = gcd(max(w, h), min(w, h))  # 함수 호출시에 큰 값,작은 값 순서로 들어가도록 하기
    answer = w * h - (w+h-tmp)

    return answer


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x
