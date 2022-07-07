def GCD(a,b):
    while b!=0:
        r = a%b
        a = b
        b = r #세 줄을 a, b = b, a%b로 줄여도 됨.
    return a

def LCM(a,b):
    return a*b//GCD(a,b)

t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    print(LCM(a,b))
"""cf) 최소공약수 구하는 함수 있음!!
import math
a = math.gcd(24, 8)
"""
#     #1등 코드
# import math
# import sys
# t=int(input())
# for _ in range(t):
#     a,b=map(int,sys.stdin.readline().split())
#     temp=math.gcd(a,b)
#     res=a//temp
#     res*=b
#     print(res)
