import sys
N = int(sys.stdin.readline().rstrip())
dp = [[0]*10 for _ in range(N+1)] # dp[i][j] : 수의 길이가 N이고 마지막 수가 j인 오르막수의 개수
m = 10007
for i in range(10): #길이가 1이고 마지막수가 0~9인 수는 각 1이므로
    dp[1][i] = 1
for i in range(2,N+1):
    for j in range(10):
        for k in range(j+1):#0<=k<=j 예를 들어,수의 길이가 2이고 마지막 수가 5인 오르막수의 개수는 수의 길이가 1이고 마지막 수가 0~4인 오르막수의 개수의 합과 같다.
            dp[i][j] += dp[i-1][k]%m
print(sum(dp[N])%m)