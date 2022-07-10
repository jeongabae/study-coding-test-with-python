import sys
import math

n = int(sys.stdin.readline().rstrip())
s = list(map(int, sys.stdin.readline().rstrip().split()))
g = math.gcd(s[0], math.gcd(s[1], s[-1])) # n은 2 또는 3이므로 요로케 하면 최대공약수 구할 수 있음.
for i in range(1, (g // 2) + 1):
    if g % i == 0: #약수 구해줌
        print(i)
print(g)