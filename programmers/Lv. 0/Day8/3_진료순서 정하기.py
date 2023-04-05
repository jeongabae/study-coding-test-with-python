def solution(emergency):
    re_em = sorted(emergency,reverse=True)
    return [re_em.index(i)+1 for i in emergency]