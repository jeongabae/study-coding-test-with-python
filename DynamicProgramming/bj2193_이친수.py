import sys
N = int(sys.stdin.readline().rstrip())
dp = [[0]*2 for _ in range(91)] # dp[i][j] 길이가 i인 이친수인데 마지막 수가 j(0or1)
dp[1][1] = 1
for i in range(2,N+1):
    for j in range(2):
        if j==0:#마지막 수가 0인 경우
            dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
        else:#마지막 수가 1인 경우
            dp[i][j] = dp[i-1][j-1]
print(sum(dp[N]))
"""내 풀이보다 더 빠른 풀이
N = int(input())

dp = [0 for _ in range(100)] # dp[i]=i자리 이친수 개수
dp[1] = 1
dp[2] = 1

for i in range(3,100):
	dp[i] = dp[i-1] + dp[i-2]

print(dp[N])
조금만 생각하면 이렇게 풀 수 있었을텐데 ㅠㅠ 내가 이 풀이를 해석해보자면
N자리 이친수 개수를 구할 때 1)2)를 더하면 답.
1) 마지막 수가 0 => dp[i-1]
N-1자리에는 0,1 둘 다 올 수 있음. 즉 d[i-1] 경우를 더해주기
2) 마지막 수가 1 => dp[i-2]
N-1자리에는 0밖에 못옴
그럼 N-2자리를 보면 N-1자리가 0이니 0,1 둘 다 가능. ->즉 d[i-2] 경우를 더해주기
"""