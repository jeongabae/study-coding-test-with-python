import math

a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))
"""유클리드호제법을 이용한 풀이
a,b = map(int,input().split())
def gcd(a,b):
    while b>0:
        a, b = b, a % b #a에 b를 넣고, b에 a%b를 넣고 나머지가 0일 때까지 반복
    return a #a가 최대공약수
def lcm(a, b):
    return a*b//gcd(a,b)

print(gcd(a,b))#최대공약수(greatest common divisor)
print(lcm(a,b))#최소공배수 (least common multiple)

#유클리드 호제법은 2개의 자연수 또는 정수의 최대공약수를 구하는 알고리즘의 하나
# 두 자연수 a,b에서 a를 b로 나눈 나머지를 r이라고 하면 a와 b의 최대공약수는 b와 r의 최대공약수와 같다 gcd(a,b) = gcd(a,r)
# 그러므로, a에 b를 넣고, b에 a%b를 넣고 나머지가 0일 때까지 반복
#gcd(24,18)=gcd(18,6)=gcd(6,0)
#gcd(18,24)=gcd(24,6)=gcd(6,0)
#호제법 : 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘

#최대공약수를 G라 했을때
#a = G*x, b = G*y. G는 최대공약수이므로 x,y는 서로소. a*b = G*G*x*y 이므로 최소공배수는 a*b//G
"""