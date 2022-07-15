import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
d = [[0]*(N+1) for _ in range(K+1)] #d[K][N] : 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수
#d[0][0] = 1
m = 1000000000
for i in range(1,K+1):
    for j in range(N+1):
        if i == 1: #d[1][N] : 0부터 j까지의 정수 1개를 더해서 그 합이 j이 되는 경우의 수는 항상 1
            d[1][j] = 1
        else:
            for last in range(j+1):
                #0부터 N까지의 정수 K개를 이용해 N을 만드는 방법은 0부터 N개까지 k-1를 만드는 개수의 합과 같음.
                d[i][j] += d[i-1][j-last] % m #만약 last를 마지막으로 더한다고 했을 떄,
                                             # last를 더하기 전에 숫자의 합은 i-last가 되고 i-1개만큼 더한 상태이다.
print(d[K][N]%m)
"""DP이용 시간복잡도 더 좋은 풀이 (근데 이 풀이는 예제를 한 번은 쭉 써봐서 유추?해야했던..)
import sys
 
input = sys.stdin.readline
 
n,k = map(int,input().split())
mod = 1000000000
d=[[0]*(k+1) for _ in range(n+1)]
 
for i in range(n+1):
    for j in range(1,k+1):
        if i==0:
            d[i][j]=1
        else:
            d[i][j] = (d[i-1][j]+d[i][j-1])%mod
print(d[-1][-1])
출처 :https://rrojin.tistory.com/42
"""
"""DP 이용 안하신 빠른 다른 분 풀이
def fac(n):
    sum =1
    for _ in range(1, n+1):
        sum *= _
    return sum

n, r = map(int, input().split())
print(fac(n+r-1)//(fac(r-1)*fac(n))%1000000000)
"""
