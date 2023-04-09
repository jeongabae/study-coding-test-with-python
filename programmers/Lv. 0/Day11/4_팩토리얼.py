import math
def solution(n):
    ans = 0
    for i in range(11):
        if math.factorial(i)>n:
            break
        ans = i
    return ans

"""다른 풀이
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k
"""