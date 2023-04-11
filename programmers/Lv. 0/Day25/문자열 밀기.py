def solution(A, B):
    ans = 0
    while ans!=len(A):
        if A==B:
            return ans
        A = A[-1]+A[:-1]
        ans+=1
    return -1


"""미친 풀이
solution=lambda a,b:(b*2).find(a)
"""

"""내 다른 풀이
from collections import deque

def solution(A, B):
    a, b = deque(A), deque(B)
    for cnt in range(len(A)):
        if a == b:
            return cnt
        a.rotate(1)
    return -1
"""

