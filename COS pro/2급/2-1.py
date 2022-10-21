def solution(shirt_size):
    answer = []
    Tdic = {'XS': 0, 'S': 0, 'M': 0, 'L': 0, 'XL': 0, 'XXL': 0}
    for size in shirt_size:
        Tdic[size] += 1
    for v in Tdic.values():
        answer.append(v)
    return answer


# The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size)

# Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")
