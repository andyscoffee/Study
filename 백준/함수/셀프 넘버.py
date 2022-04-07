# 15596 정수 N개의 합

def solve(a):
    return sum(a)

# 4673 셀프 넘버


def self(n):
    tmp = n
    while True:
        if n == 0:
            break
        tmp += n % 10
        n //= 10
    return tmp


arr = [True]*(10001)

for i in range(10001):
    if self(i) < 10001:
        arr[self(i)] = False
for i in range(10001):
    if arr[i]:
        print(i)
