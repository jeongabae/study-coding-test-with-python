T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')
    n = int(input())
    board = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = 0, 0
    cur_dir = 0
    board[x][y] = 1

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    for num in range(2, n * n + 1):
        nx = x + dx[cur_dir]
        ny = y + dy[cur_dir]

        if not in_range(nx, ny) or board[nx][ny] != 0:
            cur_dir = (cur_dir + 1) % 4
            nx = x + dx[cur_dir]
            ny = y + dy[cur_dir]

        x, y = nx, ny
        board[nx][ny] = num

    for row in board:
        print(*row)