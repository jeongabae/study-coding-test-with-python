def solution(common):
    a,b,c = common[:3]
    dif = b-a
    return common[-1]+dif if dif==c-b else common[-1]*(b//a)

"""
def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer
"""