# 럭키 스트레이트 (핵심 유형)

n = input()
length = len(n)
left, right = 0

for i in range(length / 2):
    num = int(i)
    left += num

for i in range(length / 2, length):
    num = int(n[i])
    right += num
    
if left == right:
    print('LUCKY')
else:
    print('READY')
