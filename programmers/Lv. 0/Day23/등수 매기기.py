def solution(score):
    avg = [sum(i) for i in score]
    s = sorted(avg, reverse=True)
    return [s.index(j)+1 for j in avg]
"""
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]
"""

"""
def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]
"""