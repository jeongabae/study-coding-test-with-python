def solution(angle):
    ans = 4
    if angle < 90:
        ans = 1
    elif angle == 90:
        ans = 2
    elif angle < 180:
        ans = 3

    return ans