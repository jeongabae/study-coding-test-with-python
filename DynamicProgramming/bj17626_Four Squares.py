# 내 풀이 : DP 풀이
import sys
N = int(sys.stdin.readline().rstrip())
dp = [4] * (N + 1)
dp[0] = 0
dp[1] = 1

for i in range(2, N + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)

print(dp[N])

"""내 다른 풀이 : 완전탐색 풀이
import sys

n = int(sys.stdin.readline())
minCnt = 4
s = [i ** 2 for i in range(1, 224)]

for i in s:
    for j in s:
        for k in s:
            if i==n:
                minCnt = 1
                break
            elif i+j == n:
                minCnt =min(minCnt, 2)
            elif i+j+k == n:
                minCnt =min(minCnt, 3)
print(minCnt)
"""
"""1등 풀이
n = int(input())
u = int(n**(1/2))
m = list([k**2 for k in range(1, 224)])
for i in m:
    if i == n:
        print(1)
        exit()
for i in m:
    if n-i in m:
        print(2)
        exit()
while n%4==0:
    n=n//4
if n%8==7:
    print(4)
    exit()
else:print(3)
"""