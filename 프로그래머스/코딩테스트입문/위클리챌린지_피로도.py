from itertools import permutations

def solution(k, dungeons):
    answer = 0
    data = permutations(dungeons)
    for dt in data:
        energy = k
        count = 0
        for d in dt:
            if energy >= d[0]:
                energy -= d[1]
                count += 1
        if count > answer:
            answer = count
    
    return answer

dungeons = [[80,20],[50,40],[30,10]]
k = 80
print(solution(k, dungeons))
