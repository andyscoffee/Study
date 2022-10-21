def solution(price, grade):
    answer = 0
    dc = {'S': 0.95, 'G': 0.9, 'V': 0.85}
    answer = int(dc[grade]*price)
    return answer


# The following is code to output testcase.
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")
