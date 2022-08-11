import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
T = [0]*N #걸리는 기간
P = [0]*N #
max_sum=0 #백준이가 얻을 수 있는 최대 수익

for i in range(N): #T, P 각각 입력 받기
    T[i], P[i] = map(int, input().split())

def dfs(day, P_sum):
    global max_sum
    if day==N: #0부터 인덱스 시작했으므로 N이면 퇴사
        max_sum=max(max_sum,P_sum)
        return

    elif day>N: #N을 넘어가면 퇴사날 넘어가므로 불가
        return

    dfs(day+T[day],P_sum+P[day]) #상담 하는 경우
    dfs(day+1,P_sum) #상담 안하는 경우

dfs(0,0)
print(max_sum)

"""다른 사람 풀이 : DP 풀이
# 출처 : https://jrc-park.tistory.com/119
n = int(input())
T, P = [0 for i in range(n+1)], [0 for i in range(n+1)]
for i in range(n):
    a,b = map(int, input().split())
    T[i] = a
    P[i] = b

# dp[i]는 i번째날까지 일을 했을 때, 최대값이다. 
dp =[0 for i in range(n+1)]

for i in range(len(T)-2, -1, -1):      # 역순으로 진행
    if T[i]+i <= n:       # 날짜를 초과하지 않을 경우.
        dp[i] = max(P[i] + dp[i + T[i]], dp[i+1])   
    else:                 # 날짜를 초과할 경우.
        dp[i] = dp[i+1]
print(dp[0])
"""