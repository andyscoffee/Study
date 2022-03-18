from itertools import permutations
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    data = []
    res = []
    for n in numbers:
        data += list(n)
        res += set(n)
  
    for i in range(2, len(data)+1):
        tmp = list(map(''.join, permutations(data, i)))
        res += set(tmp)
    
    res = set([i.lstrip('0') for i in res])
  
    for i in res:
        if i == '':
            continue
        if is_prime(int(i)):
            answer += 1
    return answer
