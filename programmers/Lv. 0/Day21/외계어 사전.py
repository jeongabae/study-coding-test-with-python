def solution(spell, dic):
    sort_s = sorted(spell)
    for i in dic:
        if sort_s == sorted(i):
            return 1
    return 2

"""
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
"""

"""x.issubset(y) # x가 y의 서브 set?
def solution(spell, dic):
    spell = set(spell) 
    for i in dic:
        if spell.issubset(set(i)):
            return 1 
    return 2
"""