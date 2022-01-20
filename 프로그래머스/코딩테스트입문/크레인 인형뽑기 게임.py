# 크레인 인형뽑기 게임(2019 카카오 개발자 겨울 인턴십)

def solution(board, moves):
    answer = 0
    depth = len(board)
    data = []
    now = 0

    for move in moves:
        for n in range(depth):
            if board[n][move - 1] != 0:
                now = board[n][move - 1]
                data.append(now)
                if len(data) >= 2 and now == data[-2]:
                    data.pop()
                    data.pop()
                    answer += 2
                board[n][move - 1] = 0
                break
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
