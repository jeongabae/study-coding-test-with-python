import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input()) #집의 크기 N
board = [list(map(int, input().split())) for _ in range(N)] # 집의 크기는 N×N의 격자판이고 빈칸 또는 벽을 입력 받음.
cnt = 0 #파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수

def dfs(x, y, direction): #x: x좌표, y: y좌표, direction: 파이프가 놓여진 방향. direction은 1(가로 방향으로 놓여진 경우), 2(세로 방향으로 놓여진 경우), 3(대각선 방향으로 놓여진 경우) 세가지가 있다.
    global cnt
    if x==N-1 and y==N-1: # x==N-1 and y==N-1에 도착한 경우 (문제의 좌표 상으로 N,N) 파이프의 한쪽 끝이 (N, N)으로 이동되었으므로
        cnt += 1 #파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수 1 증가 시킴

    #1. 가로 또는 대각선 방향으로 놓여진 경우 : → 방향으로 이동 가능
    if direction == 1 or direction == 3:
        if y+1<N and board[x][y+1]==0: #1.의 경우는 → 방향으로(x좌표는 그대로, y좌표는 1증가해야하므로) 가야하므로, y+1<N이어야 하고(목표 지점 (N,N)을 넘어가면 안되기 때문) 그리고 (x, y+1) 위치가 빈칸이어야 한다.
            dfs(x,y+1,1) #조건에 만족한다면 → 방향으로 이동 후 다시 그 자리에서 이동할 경우 찾기

    #2. 세로 또는 대각선 방향으로 놓여진 경우 : ↓ 방향으로 이동 가능
    if direction == 2 or direction == 3:
        if x+1<N and board[x+1][y]==0: #2.의 경우는 ↓ 방향으로(x좌표는 1증가하고, y좌표는 그대로) 가야하므로, x+1<N이어야 하고(목표 지점 (N,N)을 넘어가면 안되기 때문) 그리고 (x+1, y) 위치가 빈칸이어야 한다.
            dfs(x+1,y,2) #조건에 만족한다면 ↓ 방향으로 이동 후 다시 그 자리에서 이동할 경우 찾기

    #3. 가로 또는 세로 또는 대각선 방향으로 놓여진 경우(사실상 세 경우 모두) : ↘ 방향으로 이동 가능
    # 사실 이 경우는 if direction == 1 or if direction == 2 or direction == 3:라고 써줘야 정확한데 파이프가 놓여진 방향(direction)은 반드시 3 방향 중 하나 이므로 생략했다.
    if x+1<N and y+1<N and board[x][y+1]==0 and board[x+1][y]==0 and board[x+1][y+1]==0: #3.의 경우는 ↘ 방향으로(x, y좌표 둘 다 1증가해야하므로) 가야하므로, x+1과 y+1 모두 N보다 작아야 하고(목표 지점 (N,N)을 넘어가면 안되기 때문) 그리고 (x+1, y),(x, y+1),(x+1, y+1) 위치가 빈칸이어야 한다(왜냐면 대각선으로 놓을 경우 4칸 차지하므로)
            dfs(x+1,y+1,3)#조건에 만족한다면 ↘ 방향으로 이동 후 다시 그 자리에서 이동할 경우 찾기

dfs(0,1,1) #처음에는 한쪽 끝이 (0,1) (문제 상에서는 (1,2)이다. 내 코드의 board의 좌표는 (0,0)부터 시작하기 때문에 (0,1)) 가로(1)로 놓여져있으므로 여기서부터 탐색 시작.
print(cnt) #파이프의 한쪽 끝을 (N, N)(내 코드 상 에서는 (N-1,N-1))으로 이동시키는 방법의 수