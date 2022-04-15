# 9663
import sys

n = int(sys.stdin.readline().strip())
ans = 0
board = [0]*n  # board[i] = j <- 퀸을 (i,j) 위치에 두겠다.


def possible(x):
    for i in range(x):
        # 같은 열, 대각선 검사
        if board[x] == board[i] or abs(board[x]-board[i]) == abs(x-i):
            return False
    return True


def dfs(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            board[x] = i
            if possible(x):
                dfs(x+1)


dfs(0)
print(ans)
