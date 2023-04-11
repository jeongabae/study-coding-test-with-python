def solution(chicken):
    service = 0
    while chicken >= 10:
        div, mod = divmod(chicken, 10)
        service += div
        chicken = div+mod
    return service

"""수학자^^풀이^^(10%의 10%의 10%의 10% .... 이니까) 이런건 난 생각 못함. 괜찮음 난 천재가 아님.
def solution(chicken):
    return int(chicken*0.11111111111)
"""