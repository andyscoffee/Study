# 2020 카카오 인턴쉽 키패드 누르기
def solution(numbers, hand):
    answer = ''
    keypad = {'*': [0, 0], '0': [1, 0], '#': [2, 0], '7': [0, 1], '8': [1, 1], '9': [2, 1],
              '4': [0, 2], '5': [1, 2], '6': [2, 2], '1': [0, 3], '2': [1, 3], '3': [2, 3]}
    left = [0, 0]  # "*"에서 시작 [0] = x축 좌표, [1] = y축 좌표
    right = [2, 0]  # "#" 에서 시작
    for num in numbers:
        tmp = keypad[str(num)]
        if num in [1, 4, 7]:
            answer += "L"
            left = tmp
        elif num in [3, 6, 9]:
            answer += "R"
            right = tmp
        else:
            distl = abs(left[0]-tmp[0]) + abs(left[1]-tmp[1])
            distr = abs(right[0]-tmp[0]) + abs(right[1]-tmp[1])
            if distl == distr:
                if hand == "right":
                    answer += "R"
                    right = tmp
                else:
                    answer += "L"
                    left = tmp
            elif distl < distr:
                answer += "L"
                left = tmp
            else:
                answer += "R"
                right = tmp

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"), "LRLLLRLLRRL")
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"), "LRLLRRLLLRR")
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"), "LLRLLRLLRL")
