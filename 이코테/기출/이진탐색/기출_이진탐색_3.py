# 공유기 설치 (핵심 유형)

n, c = map(int, input().split())
data = []
res = 0

for i in range(n):
    data.append(int(input()))
data.sort()


def bin(array, start, end, c):
    while start <= end:
        gap = (start + end) // 2
        value = array[0]
        cnt = 1
        for i in range(1, n): # gap 값 이용해 공유기 설치
            if array[i] >= value + gap:
                value += array[i]
                cnt += 1
        if cnt >= c: # c개 이상 공유기를 설치할 수 있는 경우, 거리 증가
            start = gap + 1
            res = gap
        else:
            end = gap - 1
    return res

#start = 1(가능한 최소 거리), end = (data[-1] - data[0]) 가능한 최대 거리
print(bin(data, 1, (data[-1] - data[0]), c)) 
