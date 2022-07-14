import sys
N = int(sys.stdin.readline().rstrip())

dp=[[0]*10 for _ in range(101)] #dp[i][j] : 길이가 i인 계단인데 마지막 수가 j(0<=j<=9)
                                # 0으로 시작하는 수는 계단수가 아니므로 길이가 1인 0으로 끝나는 수가 없다고 설정해주면 됨.
m = 1000000000
for i in range(1,10): # 길이가 1인 계단 중에 1~9로 끝나는건 하나씩 있음.  # 0으로 시작하는 수는 계단수가 아니므로 1로 안바꿔줌.
    dp[1][i] = 1
for i in range(2,N+1):
    for j in range(10):
        # 마지막 수는 0~9이여야하므로 j-1<0(j==0일경우)이거나  j+1>9이면(j==9인 경우) 각각 j-1, j+1이 마지막 수가 안되므로..
        if j-1>=0: # 만약 j가 0이면 이 조건 만족 X
            dp[i][j] += dp[i-1][j-1]%m
        if j+1<=9: # 만약 j가 9이면 이 조건 만족 X
            dp[i][j] += dp[i-1][j+1]%m
        dp[i][j] %= m
print(sum(dp[N])%m)
"""1등분 코드
n = int(input())

DP = [[0]*10 for i in range(101)]
DP[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            DP[i][j] = DP[i-1][j+1]
        elif j == 9:
            DP[i][j] = DP[i-1][j-1]
        else:
            DP[i][j] = DP[i-1][j+1] + DP[i-1][j-1]
result = 0
for i in range(0,10):
    result += DP[n][i]

print(result%1000000000)
"""