def solution(keyinput, board):
    xy = [0, 0]
    w, h = board[0]//2, board[1]//2
    k = {'up':[0,1],'down':[0,-1],'left':[-1,0],'right':[1,0]}
    for i in keyinput:
        dx = k[i][0]
        dy = k[i][1]
        if -w<=xy[0]+dx<=w and -h<=xy[1]+dy<=h:
            xy[0]+=dx
            xy[1]+=dy
    return xy