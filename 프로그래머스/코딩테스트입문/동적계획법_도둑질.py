def solution(money):
    a = [0]*len(money) # 0번째 집을 포함 하는 경우의 DP 테이블
    b = [0]*len(money) # 0번째 집을 포함하지 않는 경우의 DP 테이블
    l = len(money)
    a[0] = money[0]
    a[1] = max(money[1], a[0])
    b[1] = max(money[1], b[0])
    
    for i in range(2, l-1):
        a[i] = max(a[i-2] + money[i], a[i-1])
        
    for i in range(2, l):
        b[i] = max(b[i-2] + money[i], b[i-1])
        
    answer = max(a[l-2],b[l-1])
    return answer

print(solution([1,2,3,1]), 4)
print(solution([1,1,4,1,4]), 8)
print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
print(solution([1000,1,0,1,2,1000,0]), 2001)
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([1,2,3]), 3)
print(solution([91,90,5,7,5,7]), 104)
print(solution([90,0,0,95,1,1]), 185)
