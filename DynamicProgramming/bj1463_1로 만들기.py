import sys
n = int(sys.stdin.readline().rstrip())
d = [0] * (n + 1)
for i in range(2, n + 1):

    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
print(d[n])
"""순위권 풀이(내 풀이보다 훨씬 빠름 약 10배..)
# dp
def dp(n):
    if n in memo:
        return memo[n]
    # 나머지를 더해준 이유는...7의 경우 2, 3으로 나누어 지지 않으므로 1을 빼는 행동을 무조건 해줘야한다.
    # 이 경우를 연산 횟수에 포함하기 위해 나머지로 더해주는 것 같음.
    m = 1 + min(dp(n // 2) + n % 2, dp(n // 3) + n % 3) # 1 + 어떤 수 = 1..
    memo[n] = m
    return m

memo = {1: 0, 2: 1}
n = int(input())
print(dp(n))
n = 10
m = 1 + min(dp(5)+0, dp(3) +1) = 1 + min(3,2) = 3

dp(5)
m = 1 + min(dp(2) + 1 , dp(1) + 2) = 1 + min(1+1, 0+2) = 3

dp(3)
m = 1 + min(dp(1)+1, dp(1)+0) = 1+min(1,0) = 1
"""