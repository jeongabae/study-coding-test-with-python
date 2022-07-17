import sys
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
dp = []
for i in range(N):
    dp.append(list(map(int, input().split())))
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]

print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))

"""1등 분 풀이
import sys
read = sys.stdin.readline

n = int(read().strip())
dp = [list(map(int, read().strip().split()))]
for i in range(1, n):
    r, g, b = map(int, read().strip().split())
    nxt_r = r + min(dp[i-1][1], dp[i-1][2])
    nxt_g = g + min(dp[i-1][0], dp[i-1][2])
    nxt_b = b + min(dp[i-1][0], dp[i-1][1])
    dp.append([nxt_r, nxt_g, nxt_b])

print(min(dp[n-1]))
"""