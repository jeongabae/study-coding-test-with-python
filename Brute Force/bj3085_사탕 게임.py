import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
board = [list(input()) for _ in range(N)]
maxCandy = 0

def cnt():
    global maxCandy
    for i in range(N):
        candy = 1 # 연속된 사탕이 몇 개 인지 세 주는 변수 초기화(처음엔 연속이 아니므로 1)
        for j in range(1, N): #행 검사
            if board[i][j] == board[i][j-1]: # 가로로 두 개가 같으면
                candy += 1 # 연속이므로 1증가
                maxCandy = max(candy, maxCandy) # 기존 연속 사탕 개수보다 많으면 maxCandy 업데이트
            else: # 가로로 두 개가 같지 않으면
                candy = 1 # 연속이 아니므로 다시 candy=1
        candy = 1 # 연속이 몇 개 인지 세 주는 변수 초기화(처음엔 연속이 아니므로 1)
        for j in range(1,N):  #열 검사
            if board[j][i] == board[j-1][i]: # 세로로 두 개가 같으면
                candy += 1  # 연속이므로 1증가
                maxCandy = max(candy, maxCandy) # 기존 연속 사탕 개수보다 많으면 maxCandy 업데이트
            else: # 세로로 두 개가 같지 않으면
                candy = 1 # 연속이 아니므로 다시 candy=1

for i in range(N):
    for j in range(N):
        if j+1 < N: # 가로 길이가 넘어가지 않는 경우에 한해
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 가로로 두 개 바꿔줌
            cnt() #최대 연속 개수 확인
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 연속 개수 확인 후 다시 보드 원래대로(다음 확인을 위해)

        if i+1 < N: # 세로 길이가 넘어가지 않는 경우에 한해
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 세로로 두 개 바꿔줌
            cnt() # 최대 연속 개수 확인
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 연속 개수 확인 후 다시 보드 원래대로(다음 확인을 위해)

print(maxCandy) # 최대 사탕 개수 출력
