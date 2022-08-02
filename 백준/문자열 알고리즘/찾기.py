# 1786

import sys
"""
이제 이 방법을 일반화 해 보자. T의 i번 문자에서 시작하는 매칭을 검사하던 중 T[i+j-1] ≠ P[j]임을 발견했다고 하자. 
이렇게 P의 j번 문자에서 매칭이 실패한 경우, 
P[1…k] = P[j-k…j-1]을 만족하는 최대의 k(≠j-1)에 대해 T의 i+j-1번 문자와 P의 k+1번 문자부터 비교를 계속해 나가면 된다.

이 최대의 k를 j에 대한 함수라고 생각하고, 1～m까지의 각 j값에 대해 최대의 k를 미리 계산해 놓으면 편리할 것이다. 
이를 전처리 과정이라고 부르며, O(m)에 완료할 수 있다.
이러한 원리를 이용하여, T와 P가 주어졌을 때, 문자열 매칭 문제를 해결하는 프로그램을 작성하시오.
"""


def getPi():
    pi = [0 for _ in range(0, len(P))]
    j = 0

    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]

        if (P[i] == P[j]):
            j += 1
            pi[i] = j
    return pi


def KMP(pi):
    result = []
    cnt = 0
    j = 0
    for i in range(0, len(T)):

        while j > 0 and T[i] != P[j]:
            j = pi[j - 1]

        if T[i] == P[j]:
            if j == (len(P) - 1):
                result.append(i - len(P) + 2)
                cnt += 1
                j = pi[j]
            else:
                j += 1

    print(cnt)
    for l in result:
        print(l)


T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
KMP(getPi())
