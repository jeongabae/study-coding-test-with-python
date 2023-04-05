def solution(dot):
    x, y = dot[0], dot[1] #x,y = dot
    ans = 4
    if x>0 and y>0:
        ans = 1
    elif x<0 and y>0:
        ans = 2
    elif x<0 and y<0:
        ans = 3
    return ans

"""신기한 풀이..ㅋ
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]
"""

"""
def solution(dot):
    x,y = dot
    if x*y>0:
        return 1 if x>0 else 3
    else:
        return 4 if x>0 else 2
"""