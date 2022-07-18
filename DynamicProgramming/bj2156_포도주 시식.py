import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
a = [0]+[int(input()) for _ in range(n)]
dp = a.copy()

if n>1: #요 if문 빼먹어서 indexerror판정났었음. n=1인 경우는 dp[2] += dp[1]가 안되기 때문에 if문 꼭 필요.
    dp[2] += dp[1]

for i in range(3,n+1):
    dp[i] = max(dp[i-1],dp[i-2]+a[i],dp[i-3]+a[i-1]+a[i])
print(dp[n])
"""
경우 1) 0번 연속해서 마실 경우 a[i] 마시지 x
-> dp[i] = dp[i-1]
경우 2) 1번 연속해서 마실 경우 a[i-1] 마시지 x
-> dp[i] = dp[i-2] + a[i]
경우 3) 2번 연속해서 마실 경우 a[i-2] 마시지 x, a[i-1]이랑 a[i] 마심
-> dp[i] = dp[i-2] + a[i-1] +a[i]
경우 1,2,3 중 최대를 dp[i]에 저장
"""