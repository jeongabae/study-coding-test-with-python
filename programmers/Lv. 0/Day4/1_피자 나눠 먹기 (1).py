def solution(n):
    a = n//7
    return a+1 if n%7 else a


"""
def solution(n):
    return (n - 1) // 7 + 1
"""

"""
def solution(n):
    return n//7 + (n%7 != 0)
"""

"""
import math

def solution(n):
    return math.ceil(n/7)
"""