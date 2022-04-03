# 달팽이는 올라가고 싶다 2869
import math
a, b, v = map(int, input().split())
n = (v-a)/(a-b)
print(math.ceil(n+1))


# 큰 수 A+B
"""
파이썬은 이렇게 큰 수도 지원을 해줘서 그냥 두 수 입력받아 더하기로 제출해 통과했는데, 
c++ 사용자들이 문자열 등을 사용해 길게 풀어낸 코드를 바라보고 있으니 좀 민망했다.
"""
map(int, input().split())
print(a+b)
