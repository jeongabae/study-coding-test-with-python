import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
score = [int(input()) for _ in range(n)]

if n>=3:
    dp = [score[0], score[0] + score[1],max(score[0], score[1]) + score[2]] + [0] * (n - 3)
    for i in range(3, n):
        dp[i] = max(dp[i-2]+score[i], dp[i-3] + score[i-1]+score[i])
    print(dp[-1])
else:
    print(sum(score))