# You may use import as below.
#import math

def solution(pos):
    # Write code here.
    possible = [(1, 2), (1, -2), (2, 1), (2, -1),
                (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    answer = 0
    row = int(pos[1])
    col = ord(pos[0])-65+1  # A = 65, 1부터시작하기에 +1

    for i in possible:
        nr = row + i[0]
        nc = col + i[1]
        if 1 <= nr <= 8 and 1 <= nc <= 8:
            answer += 1
    return answer


# The following is code to output testcase.
pos = "A7"
ret = solution(pos)

# Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
