def solution(board):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    n = len(board)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    if 0 <= i - dx[k] < n and 0 <= j - dy[k] < n and board[i - dx[k]][j - dy[k]] != 1: #주의 여기서 범위 안에 있는지 확인 전에  board[i - dx[k]][j - dy[k]] != 1조건 먼저쓰면 오류남. 범위 확인하고 써줘야함.
                        board[i - dx[k]][j - dy[k]] = 2

    return sum(i.count(0) for i in board)

"""
ef solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
"""

"""
def solution(board):
    N = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    # 지뢰 설치
    boom = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                boom.append((i,j)) # 지뢰일때의 인덱스 append
                    
    # 지뢰가 설치된 곳 주변에 폭탄 설치
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1

    # 폭탄이 설치되지 않은 곳만 카운팅
    count = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                count += 1
    return count
"""