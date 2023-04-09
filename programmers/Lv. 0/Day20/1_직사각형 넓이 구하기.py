def solution(dots):
    x = [i[0] for i in dots]
    y = [i[1] for i in dots]
    return abs(max(x)-min(x))*abs(max(y)-min(y))

"""
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
"""