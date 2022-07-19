import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
d = [1]*N #d[i] : A[i]를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
for i in range(N):
    for j in range(i):
        if A[i] < A[j] and d[i] < d[j]+1: # 감소하는 수열이여야하므로 A[i] < A[j]
                                          # 가장 긴 수열을 구하는 것이므로 d[i] < d[j]+1
                                          # d[j]+1한 값이 지금 d[i]보다 크다면 더 긴 수열을 만들 수 있다는 것이니까 아래처럼 d[i]를 바꿔줌.
            d[i] = d[j]+1
print(max(d))