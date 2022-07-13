import sys
def input():
    return sys.stdin.readline().rstrip()

T=int(input())
m= 1000000009
dp=[[0]*3 for _ in range(100001)]
# dp[i][0]은 1로 끝나는 경우, dp[i][1]은 2로 끝나는 경우, dp[i][2]은 3로 끝나는 경우
dp[1]=[1,0,0] # 1 = 1
dp[2]=[0,1,0] # 2 = 2
dp[3]=[1,1,1] # 3 = 2+1 = 1 + 2 = 3

for i in range(4,100001):
    dp[i][0]=dp[i-1][1]%m+dp[i-1][2]%m #dp[i][0]는(1로 끝나는 경우) dp[i-1][1](2로 끝나는 경우) + dp[i-1][0] (3으로 끝나는 경우)
    dp[i][1]=dp[i-2][0]%m+dp[i-2][2]%m #dp[i][1]는(2로 끝나는 경우) dp[i-1][0](1로 끝나는 경우) + dp[i-1][0] (3으로 끝나는 경우)
    dp[i][2]=dp[i-3][0]%m+dp[i-3][1]%m #dp[i][2]는(3로 끝나는 경우) dp[i-1][0](1로 끝나는 경우) + dp[i-1][1] (2으로 끝나는 경우)

for i in range(T):
    n=int(input())
    print(sum(dp[n]) % m)