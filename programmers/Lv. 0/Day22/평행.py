from itertools import combinations

def solution(dots):
    c = list(combinations(dots, 2))
    for i in range(len(c) // 2):
        dx1, dy1 = c[i][0][0] - c[i][1][0], c[i][0][1] - c[i][1][1]
        dx2, dy2 = c[-(i+1)][0][0] - c[-(i+1)][1][0], c[-(i+1)][0][1] - c[-(i+1)][1][1]
        if dx1*dy2 == dy1*dx2:
           return 1
    return 0