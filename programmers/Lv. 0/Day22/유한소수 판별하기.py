from math import gcd

def solution(a, b):
    b //= gcd(a, b)
    for i in [2, 5]:
        while b % i == 0: #while not b % i:
            b //= i
    return 1 if b == 1 else 2


"""내꺼랑 비슷한 풀이
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2
"""