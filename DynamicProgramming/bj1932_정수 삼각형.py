import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = a[0][0]
idx = 0
for i in range(1,n):
    for j in range(i+1):
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])+a[i][j]
print(max(dp[n-1]))
"""
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있으므로 
dp[i-1][j],dp[i-1][j-1] 중 큰 것을 고르고 거기다가 현재 수를 더한 값이 dp[i][j] 선택 시 가장 큰 수가 된다.
"""
"""다른분 풀이
 출처 : https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-1932-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
n = int(input())
dp = []

for i in range(n) :                            ## 입력값 이차원리스트 형태로 dp테이블에 저장하기
    dp.append(list(map(int,input().split())))

print(dp)
print(dp[1][0])

for i in range(1,n) :                           ## 행을 기준으로 for문 구성
    for j in range(0,i+1) :                     ## 열을 기준으로 for문 구성
        if j == 0 :
            dp[i][0] += dp[i-1][0]              # 0열끼리 더하기
        elif j == i :
            dp[i][j] += dp[i-1][j-1]            # 마지막 열끼리 더하기
        else :
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])    # 두 화살표중 더 큰 경우 받아들이기

print(max(dp[n-1]))                 # n-1행에서의 최댓값 출력
"""