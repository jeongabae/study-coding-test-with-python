import sys
def input():
    return sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    n = int(input())
    a = [[0] * n]
    for _ in range(2):
        a.append(list(map(int, input().split())))
    dp = a
    for i in range(1,n):
        dp[0][i] = max(dp[0][i-1],dp[1][i-1],dp[2][i-1])
        dp[1][i] = max(dp[0][i - 1], dp[2][i - 1])+a[1][i]
        dp[2][i] = max(dp[0][i - 1] , dp[1][i - 1])+a[2][i]
    print(max(dp[0][n-1],dp[1][n-1],dp[2][n-1]))
"""
경우 1) dp[0][i] : i열에서 스티커를 뜯지 않는 경우
-> i-1열에서 위쪽 혹은 아래쪽 스티커를 뜯거나 둘 다 안 뜯어도 상관없으므로 세 가지 경우 중 큰 값을 골라준다.
 dp[0][i] = max(dp[0][i-1],dp[1][i-1],dp[2][i-1])
경우 2) dp[1][i] : i열에서 위쪽 스티커 뜯는 경우
-> i-1열에서 아래쪽 스티커를 뜯거나 둘 다 안 뜯는 경우만 가능. 둘 중 큰 값을 골라줌.
 dp[1][i] = max(dp[0][i - 1], dp[2][i - 1])+a[1][i]
경우 3) dp[2][i] : i열에서 아래쪽 스티커 뜯는 경우
-> i-1열에서 위쪽 스티커를 뜯거나 둘 다 안 뜯는 경우만 가능. 둘 중 큰 값을 골라줌.
dp[2][i] = max(dp[0][i - 1] , dp[1][i - 1])+a[2][i]
마지막으로 출력할 때는 제일 큰 값 출력해야하므로, max(dp[0][n-1],dp[1][n-1],dp[2][n-1]
"""

""" 다른 분 풀이
# 출처 : https://fre2-dom.tistory.com/281
import sys

t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for _ in range(t):
    n = int(sys.stdin.readline())
    m1 = list(map(int, sys.stdin.readline().split())) # 첫 번째 줄 스티커의 점수
    m2 = list(map(int, sys.stdin.readline().split())) # 두 번째 줄 스티커의 점수

    # 반복문을 통해 각 스티커 인덱스의 최댓값을 구한다.
    for i in range(1, n):
        # 인덱스가 1일때 최댓값은 이전 대각선의 스티커 점수이다.
        if i == 1:
            m1[1] += m2[0]
            m2[1] += m1[0]

        # 인덱스가 1보다 클 경우에는
        # 두칸 전에 스티커 값과 이전 스티커 값 중에서 큰 값과 현재 스티커의 값을 더한 값이 최댓값이 된다.
        else:
            m1[i] = max(m2[i - 1], m2[i - 2]) + m1[i]
            m2[i] = max(m1[i - 1], m1[i - 2]) + m2[i]

    print(max(m1[n - 1], m2[n - 1]))
"""