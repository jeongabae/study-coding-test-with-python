import sys
import math
from itertools import combinations
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n,*s = map(int,sys.stdin.readline().rstrip().split())
    a =list(combinations(s,2))
    """위 두 줄을 아래처럼 써도 똑같음.
    n = list(map(int,sys.stdin.readline().rstrip().split()))
    a =list(combinations(n[1:],2))
    """
    print(sum([math.gcd(i[0],i[1]) for i in a]))

"""
def gcd(a, b):
    return a if b==0 else gcd(b, a%b)

T = int(input())

for i in range(T):
    n, *a = map(int, input().split())
    s = 0
    for j in range(0, n-1):
        for k in range(j+1, n):
            s += gcd(a[j], a[k])
    print(s)
    
"""