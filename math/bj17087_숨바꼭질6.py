#모든 |A1-S|, |A2-S|, ...의 최소공약수를 구하면됨.
import sys
import math
N, S = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
print(math.gcd(*[abs(i - S) for i in A]))

"""2등 코드
import math

s = int(input().split()[1])
print(math.gcd(*(int(v) - s for v in input().split())))
"""