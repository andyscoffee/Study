def func(record):
    if record == 0:
        return 1
    elif record == 1:
        return 2
    return 0


def solution(recordA, recordB):
    cnt = 0
    for i in range(len(recordA)):
        if recordA[i] == recordB[i]:
            continue
        elif recordA[i] == func(recordB[i]):
            cnt = cnt + 3
        else:
            if cnt == 0:
                continue
            cnt = cnt - 1
    return cnt


# 0,1,2 가위 바위 보
# The following is code to output testcase. The code below is correct and you shall correct solution function.
recordA = [2, 0, 0, 0, 0, 0, 1, 1, 0, 0]
recordB = [0, 0, 0, 0, 2, 2, 0, 2, 2, 2]
ret = solution(recordA, recordB)


# Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
