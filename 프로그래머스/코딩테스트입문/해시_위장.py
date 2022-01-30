def solution(clothes):
    answer = 1
    dic  = {}
    
    for i in range(len(clothes)):
        val, part = clothes[i]
        if part not in dic.keys():
            dic[part] = []
            dic[part].append(val)
        else:
            dic[part].append(val)
    # 옷들 중 같은 파트의 옷은 고르지 않은 채 최소 하나의 옷을 고르는 경우의 수 : (1번 파트 옷의 가짓수+1)*(2번 파트 옷의 가짓수+1) * ....(n번 파트 옷의 가짓수 +1) -1
    for i in dic.keys():
        answer *=(len(dic[i])+1)
    
    return answer-1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
