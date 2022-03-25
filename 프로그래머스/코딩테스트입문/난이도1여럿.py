# 약수의 합
import math


def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer


# 서울에서 김서방 찾기
def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = "김서방은 " + str(i) + "에 있다"
    return answer


# 수박수박수박수박수박수?
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"
    return answer


# 문자열을 정수로 바꾸기
def solution(s):
    return int(s)


# 최갯값과 최솟값
def solution(s):
    answer = ''
    tmp = list((s.split(" ")))
    for i in range(len(tmp)):
        tmp[i] = int(tmp[i])
    tmp.sort()
    answer += str(tmp[0])+" "+str(tmp[-1])
    return answer


# 최솟값 만들기
def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for a, b in zip(A, B):
        answer += a*b
    return answer


# 제일 작은 수 제거하기
def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0:
        return [-1]
    return arr


# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    data = str(n)
    for i in range(1, len(data)+1):
        answer.append(int(data[-i]))
    return answer


# 이상한 문자 만들기
def solution(s):
    answer = ''
    tmp = s.split(" ")
    for w in tmp:
        for l in range(len(w)):
            if l % 2 == 0:
                answer += w[l].upper()
            else:
                answer += w[l].lower()
        answer += " "
    return answer[:-1]  # 마지막 공백 제거


# 문자열 내 맘대로 정렬하기
def solution(strings, n):
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer


# 문자열 내 p와 y의 개수
def solution(s):
    answer = False
    p, y = 0, 0
    for i in s:
        if i == "p" or i == "P":
            p += 1
        elif i == "Y" or i == "y":
            y += 1
    if p == y:
        return True
    return answer


# 문자열 내림차순으로 배치하기
def solution(s):
    tmp = sorted(list(s), reverse=True)
    answer = ''.join(tmp)
    return answer


# 문자열 다루기 기본
def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
    return answer


# 소수 찾기 (설명엔 없는데 에라토스테네스의 채)


def solution(n):
    answer = 0
    arr = [True for i in range(n+1)]
    arr[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i*j] = False
                j += 1
    for i in range(2, n+1):
        if arr[i]:
            answer += 1
    return answer


# 자릿수 더하기
def solution(n):
    answer = 0
    N = list(str(n))
    for i in N:
        answer += int(i)
    return answer


# 최대공약수와 최소공배수
def solution(n, m):
    answer = []
    big = max(n, m)
    small = min(n, m)
    while True:
        r = big % small
        if r == 0:
            answer.append(small)
            break
        big = small
        small = r
    answer.append((n*m)//small)
    return answer


# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return sorted(answer)
