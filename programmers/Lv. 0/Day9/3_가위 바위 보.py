def solution(rsp):
    win = {2:'0', 0:'5', 5:'2'}
    return ''.join([win[int(i)] for i in rsp])


"""똑같은(비슷한) 풀이
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
"""