def solution(n, t):
    for i in range(t):
        n*=2
    return n

"""정수를 2배로 곱하거나 나누어 계산해 주는 비트단위시프트연산자 <<, >>
def solution(n, t):
    return n << t
"""

"""n곱하기 2^t : 비트연산자랑 같음
def solution(n, t):
    return n*(2**t)
"""